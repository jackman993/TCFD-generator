import streamlit as st
import anthropic
from pathlib import Path
import sys

# 加入 TCFD_Table 路徑
sys.path.append(str(Path(__file__).parent / "TCFD_Table"))
from tcfd_01_transformation import create_table as create_01
from tcfd_02_market import create_table as create_02
from tcfd_03_physical import create_table as create_03
from tcfd_04_temperature import create_table as create_04
from tcfd_05_resource import create_table as create_05

# ============ 設定 ============
# API Key 從側邊欄輸入
API_KEY = st.sidebar.text_input("🔑 請輸入 Claude API Key", type="password")
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# 專家角色
EXPERT_ROLE = "你是 ESG 的 GRI 和 TCFD 專家。"

# 5 個表格設定
TABLES = [
    {
        "name": "01 轉型風險",
        "create": create_01,
        "prompt": EXPERT_ROLE + """針對「{industry}」進行 TCFD 轉型風險分析，用繁體中文回答。
請詳細分析，每個重點 80~120 字，包含具體數據、比例、時程。
輸出 2 行，每行用 ||| 分隔三欄，每欄 3 點用分號(;)隔開：
風險描述|||財務影響|||因應措施
第1行：政策與法規風險
第2行：綠色產品與科技風險
只輸出 2 行，不要其他文字。"""
    },
    {
        "name": "02 市場風險",
        "create": create_02,
        "prompt": EXPERT_ROLE + """針對「{industry}」進行 TCFD 市場風險分析，聚焦 2026 年以後趨勢，用繁體中文回答。
請詳細分析，每個重點 80~120 字，包含具體數據、比例、時程。
輸出 2 行，每行用 ||| 分隔三欄，每欄 3 點用分號(;)隔開：
風險描述|||財務影響|||因應措施
第1行：消費者偏好變化風險
第2行：市場需求變化風險
只輸出 2 行，不要其他文字。"""
    },
    {
        "name": "03 實體風險",
        "create": create_03,
        "prompt": EXPERT_ROLE + """針對「{industry}」進行 TCFD 實體風險分析，用繁體中文回答。
請詳細分析，每個重點 80~120 字，包含具體數據、比例、時程。
輸出 2 行，每行用 ||| 分隔三欄，每欄 3 點用分號(;)隔開：
風險描述|||財務影響|||因應措施
第1行：極端氣候事件風險
第2行：長期氣候變遷風險
只輸出 2 行，不要其他文字。"""
    },
    {
        "name": "04 溫升風險",
        "create": create_04,
        "prompt": EXPERT_ROLE + """針對「{industry}」進行 TCFD 溫升情境風險分析，用繁體中文回答。
請詳細分析，每個重點 80~120 字，包含具體數據、比例、時程。
輸出 2 行，每行用 ||| 分隔三欄，每欄 3 點用分號(;)隔開：
風險描述|||財務影響|||因應措施
第1行：升溫1.5°C情境風險
第2行：升溫2°C以上情境風險
只輸出 2 行，不要其他文字。"""
    },
    {
        "name": "05 資源效率",
        "create": create_05,
        "prompt": EXPERT_ROLE + """針對「{industry}」進行 TCFD 資源效率機會分析，用繁體中文回答。
請詳細分析，每個重點 80~120 字，包含具體數據、比例、時程。
輸出 2 行，每行用 ||| 分隔三欄，每欄 3 點用分號(;)隔開：
機會描述|||潛在效益|||行動方案
第1行：能源效率提升機會
第2行：資源循環利用機會
只輸出 2 行，不要其他文字。"""
    },
]

# ============ UI ============
st.set_page_config(page_title="TCFD 生成器", page_icon="📊", layout="centered")
st.title("📊 TCFD 氣候風險分析")

industry = st.text_input("請輸入您的產業", placeholder="例如：鋁建材業")

if st.button("生成 5 個 TCFD 表格", type="primary", use_container_width=True):
    
    if not API_KEY:
        st.error("請先在左側輸入 API Key")
        st.stop()
    
    if not industry:
        st.error("請輸入產業")
        st.stop()
    
    client = anthropic.Anthropic(api_key=API_KEY)
    results = []
    
    for idx, table in enumerate(TABLES):
        st.info(f"⏳ {table['name']}...")
        
        # LLM
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": table["prompt"].format(industry=industry)}]
        )
        llm_output = response.content[0].text.strip()
        lines = [line.strip() for line in llm_output.split('\n') if line.strip() and '|||' in line]
        
        # 偵錯：如果沒有解析到資料
        if len(lines) == 0:
            st.warning(f"⚠️ {table['name']} LLM 回傳格式異常，重試中...")
            with st.expander(f"LLM 原始回應 - {table['name']}"):
                st.code(llm_output)
            # 重試一次
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": table["prompt"].format(industry=industry)}]
            )
            llm_output = response.content[0].text.strip()
            lines = [line.strip() for line in llm_output.split('\n') if line.strip() and '|||' in line]
        
        # 生成 PPTX
        filepath = table["create"](lines, industry)
        results.append({"name": table["name"], "path": filepath})
        st.success(f"✅ {table['name']} 完成（{len(lines)} 行資料）")
    
    # 下載區
    st.subheader("📁 下載")
    for r in results:
        with open(r['path'], "rb") as f:
            st.download_button(f"⬇️ {r['name']}", f.read(), file_name=r['path'].name, key=r['name'], use_container_width=True)
