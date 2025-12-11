#!/usr/bin/env python3
"""
TCFD 氣候風險分析與 Claude AI 整合平台
主要入口點 - Homepage
啟動方式: streamlit run app.py
"""

import streamlit as st

# ============ 頁面設定 ============
st.set_page_config(
    page_title="TCFD 氣候風險平台",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============ 自定義 CSS ============
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700&display=swap');
    
    .main-header {
        font-family: 'Noto Sans TC', sans-serif;
        background: linear-gradient(135deg, #1a472a 0%, #2d5a27 50%, #4a7c59 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    }
    
    .main-header h1 {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    .feature-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #e0e0e0;
        height: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        border-color: #2d5a27;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1a472a;
        margin-bottom: 0.8rem;
    }
    
    .feature-desc {
        color: #555;
        line-height: 1.6;
    }
    
    .stat-box {
        background: linear-gradient(135deg, #2d5a27, #4a7c59);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #2d5a27, #4a7c59);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #1a472a, #2d5a27);
        box-shadow: 0 4px 15px rgba(45,90,39,0.4);
    }
</style>
""", unsafe_allow_html=True)

# ============ Header ============
st.markdown("""
<div class="main-header">
    <h1>🌍 TCFD 氣候風險分析平台</h1>
    <p>Task Force on Climate-related Financial Disclosures</p>
    <p>企業氣候風險評估與節能減碳智能解決方案</p>
</div>
""", unsafe_allow_html=True)

# ============ 統計數據 ============
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">9</div>
        <div class="stat-label">風險項目分析</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">35%</div>
        <div class="stat-label">平均節能效益</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">3</div>
        <div class="stat-label">創新技術方案</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">2.5年</div>
        <div class="stat-label">平均投資回收</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============ 功能卡片 ============
st.markdown("## 📋 平台功能")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">TCFD 風險分析表</div>
        <div class="feature-desc">
            完整的氣候風險評估框架，涵蓋設備、員工、能源三大面向，
            包含風險描述、影響評估與適應措施建議。
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("查看風險分析表", key="btn_tcfd", use_container_width=True):
        st.switch_page("pages/1_📊_TCFD風險分析表.py")

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">Claude AI 助手</div>
        <div class="feature-desc">
            整合 Claude API 的智能對話系統，支援文件、圖片上傳，
            可快速生成 TCFD 報告與風險分析。
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("開啟 AI 助手", key="btn_ai", use_container_width=True):
        st.switch_page("pages/2_🤖_Claude_AI助手.py")

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <div class="feature-title">數據分析工具</div>
        <div class="feature-desc">
            風險矩陣視覺化、節能效益計算器、
            ROI 分析工具，協助決策者評估投資報酬。
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("使用分析工具", key="btn_analysis", use_container_width=True):
        st.switch_page("pages/3_📈_數據分析工具.py")

st.markdown("<br>", unsafe_allow_html=True)

# ============ TCFD 簡介 ============
st.markdown("## 🌱 關於 TCFD")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    **TCFD（氣候相關財務揭露工作小組）** 是由金融穩定委員會（FSB）設立的國際倡議，
    旨在為企業提供氣候相關風險與機會的揭露框架。
    
    ### 四大核心要素：
    
    | 要素 | 說明 |
    |------|------|
    | **治理** | 董事會與管理層對氣候風險的監督機制 |
    | **策略** | 氣候風險對業務、策略與財務規劃的影響 |
    | **風險管理** | 識別、評估與管理氣候風險的流程 |
    | **指標與目標** | 評估氣候風險的量化指標與減碳目標 |
    """)

with col2:
    st.markdown("""
    ### 📌 為什麼重要？
    
    - 🏦 金融監管機構要求
    - 📈 投資人關注 ESG 績效
    - 🌍 2050 淨零排放目標
    - 💰 降低氣候轉型風險
    - 🏆 提升企業競爭力
    """)

# ============ 側邊欄 ============
with st.sidebar:
    st.markdown("### 🔗 快速連結")
    st.page_link("app.py", label="🏠 首頁", icon="🏠")
    st.page_link("pages/1_📊_TCFD風險分析表.py", label="📊 TCFD 風險分析表")
    st.page_link("pages/2_🤖_Claude_AI助手.py", label="🤖 Claude AI 助手")
    st.page_link("pages/3_📈_數據分析工具.py", label="📈 數據分析工具")
    
    st.divider()
    
    st.markdown("### ℹ️ 系統資訊")
    st.caption("版本: 1.0.0")
    st.caption("最後更新: 2025-12-09")
    
    st.divider()
    
    st.markdown("### 📚 參考資源")
    st.markdown("[TCFD 官方網站](https://www.fsb-tcfd.org/)")
    st.markdown("[金管會 ESG 專區](https://www.fsc.gov.tw/)")

# ============ Footer ============
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>© 2025 TCFD 氣候風險分析平台 | 整合 Claude AI 技術</p>
    <p>🌱 推動企業永續發展，邁向淨零未來</p>
</div>
""", unsafe_allow_html=True)


