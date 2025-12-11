#!/usr/bin/env python3
"""
TCFD 數據分析工具
風險矩陣視覺化、效益計算器
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="數據分析工具",
    page_icon="📈",
    layout="wide"
)

# ============ 側邊欄 ============
with st.sidebar:
    st.markdown("### 🔗 快速連結")
    st.page_link("app.py", label="🏠 首頁")
    st.page_link("pages/1_📊_TCFD風險分析表.py", label="📊 TCFD 風險分析表")
    st.page_link("pages/2_🤖_Claude_AI助手.py", label="🤖 Claude AI 助手")
    st.page_link("pages/3_📈_數據分析工具.py", label="📈 數據分析工具")
    
    st.divider()
    
    st.markdown("### 📊 分析選項")
    analysis_type = st.radio(
        "選擇分析類型",
        ["風險矩陣", "效益分析", "趨勢預測", "自訂數據"]
    )

st.title("📈 TCFD 數據分析工具")
st.caption("風險矩陣視覺化 | 節能效益計算 | ROI 分析")

# ============ 風險數據 ============
risk_df = pd.DataFrame({
    'category': ['設備', '設備', '設備', '員工', '員工', '員工', '能源', '能源', '能源'],
    'risk_type': ['設備過熱', '冷卻能耗', '材料老化', '健康風險', '空氣品質', '通勤影響', 
                 '尖峰用電', '供應不穩', '價格波動'],
    'impact_score': [9, 7, 6, 8, 5, 4, 9, 6, 7],
    'probability': [0.7, 0.8, 0.6, 0.5, 0.4, 0.6, 0.9, 0.5, 0.7],
    'cost_impact': [150, 80, 50, 30, 15, 10, 200, 100, 60],
    'mitigation_effectiveness': [0.7, 0.35, 0.5, 0.6, 0.8, 0.4, 0.6, 0.7, 0.3]
})

solution_df = pd.DataFrame({
    'technology': ['AI能耗監控', '被動式設計', '智能樓宇管理'],
    'energy_saving_pct': [20, 35, 30],
    'carbon_reduction_pct': [20, 40, 35],
    'investment': [50, 200, 80],
    'roi_years': [1.8, 3.5, 2.2]
})

# ============ 風險矩陣 ============
if analysis_type == "風險矩陣":
    st.markdown("### 🎯 氣候風險矩陣")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # 建立風險矩陣圖
        fig = px.scatter(
            risk_df,
            x='probability',
            y='impact_score',
            size='cost_impact',
            color='category',
            hover_name='risk_type',
            hover_data={
                'probability': ':.0%',
                'impact_score': True,
                'cost_impact': ':,.0f',
                'mitigation_effectiveness': ':.0%'
            },
            labels={
                'probability': '發生機率',
                'impact_score': '影響程度 (1-10)',
                'cost_impact': '潛在損失 (百萬元)',
                'category': '風險類別',
                'mitigation_effectiveness': '減緩有效性'
            },
            title='TCFD 氣候風險矩陣',
            color_discrete_map={
                '設備': '#e74c3c',
                '員工': '#3498db',
                '能源': '#2ecc71'
            }
        )
        
        # 添加風險區域
        fig.add_shape(type="rect", x0=0.5, y0=7, x1=1.0, y1=10,
                     fillcolor="red", opacity=0.1, line_width=0)
        fig.add_shape(type="rect", x0=0, y0=7, x1=0.5, y1=10,
                     fillcolor="orange", opacity=0.1, line_width=0)
        fig.add_shape(type="rect", x0=0.5, y0=0, x1=1.0, y1=7,
                     fillcolor="orange", opacity=0.1, line_width=0)
        fig.add_shape(type="rect", x0=0, y0=0, x1=0.5, y1=7,
                     fillcolor="green", opacity=0.1, line_width=0)
        
        fig.add_annotation(x=0.75, y=9, text="高風險區", showarrow=False, font=dict(color="red"))
        fig.add_annotation(x=0.25, y=9, text="中高風險", showarrow=False, font=dict(color="orange"))
        fig.add_annotation(x=0.75, y=3, text="中風險", showarrow=False, font=dict(color="orange"))
        fig.add_annotation(x=0.25, y=3, text="低風險區", showarrow=False, font=dict(color="green"))
        
        fig.update_layout(
            height=500,
            xaxis=dict(range=[0, 1], tickformat='.0%'),
            yaxis=dict(range=[0, 10])
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 📊 風險摘要")
        
        high_risk = risk_df[risk_df['impact_score'] >= 8]
        st.error(f"🔴 高影響風險: {len(high_risk)} 項")
        for _, row in high_risk.iterrows():
            st.write(f"• {row['risk_type']} (損失: {row['cost_impact']}百萬)")
        
        medium_risk = risk_df[(risk_df['impact_score'] >= 5) & (risk_df['impact_score'] < 8)]
        st.warning(f"🟠 中影響風險: {len(medium_risk)} 項")
        
        low_risk = risk_df[risk_df['impact_score'] < 5]
        st.success(f"🟢 低影響風險: {len(low_risk)} 項")
        
        st.markdown("---")
        st.metric("總潛在損失", f"{risk_df['cost_impact'].sum()} 百萬元")
        st.metric("平均減緩效果", f"{risk_df['mitigation_effectiveness'].mean():.0%}")

# ============ 效益分析 ============
elif analysis_type == "效益分析":
    st.markdown("### 💰 節能方案效益分析")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 節能效益比較
        fig_saving = go.Figure()
        
        fig_saving.add_trace(go.Bar(
            name='節能效益',
            x=solution_df['technology'],
            y=solution_df['energy_saving_pct'],
            marker_color='#3498db'
        ))
        
        fig_saving.add_trace(go.Bar(
            name='減碳效益',
            x=solution_df['technology'],
            y=solution_df['carbon_reduction_pct'],
            marker_color='#2ecc71'
        ))
        
        fig_saving.update_layout(
            title='各方案節能減碳效益比較',
            yaxis_title='百分比 (%)',
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig_saving, use_container_width=True)
    
    with col2:
        # ROI 分析
        solution_df['annual_saving'] = solution_df['investment'] / solution_df['roi_years']
        solution_df['10yr_benefit'] = solution_df['annual_saving'] * 10 - solution_df['investment']
        
        fig_roi = px.bar(
            solution_df,
            x='technology',
            y=['investment', '10yr_benefit'],
            title='投資與10年淨效益',
            labels={'value': '金額 (百萬元)', 'technology': '技術方案'},
            color_discrete_map={'investment': '#e74c3c', '10yr_benefit': '#2ecc71'},
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig_roi, use_container_width=True)
    
    # 詳細數據表
    st.markdown("#### 📋 方案詳細數據")
    
    display_df = solution_df.copy()
    display_df.columns = ['技術方案', '節能(%)', '減碳(%)', '投資(百萬)', 'ROI(年)', '年效益(百萬)', '10年淨效益(百萬)']
    
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )
    
    # 投資建議
    st.markdown("#### 💡 投資建議")
    best_roi = solution_df.loc[solution_df['roi_years'].idxmin()]
    best_benefit = solution_df.loc[solution_df['10yr_benefit'].idxmax()]
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"🚀 最快回收: **{best_roi['technology']}** ({best_roi['roi_years']}年)")
    with col2:
        st.success(f"💎 最高效益: **{best_benefit['technology']}** (10年淨效益 {best_benefit['10yr_benefit']:.0f}百萬)")

# ============ 趨勢預測 ============
elif analysis_type == "趨勢預測":
    st.markdown("### 📈 能源成本趨勢預測")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        base_cost = st.number_input("基準年能源成本 (萬元)", value=1000, step=100)
        growth_rate = st.slider("年增長率 (%)", 0, 20, 5)
        tech_saving = st.slider("技術節能率 (%)", 0, 50, 25)
        years = st.slider("預測年數", 5, 20, 10)
    
    with col2:
        # 生成預測數據
        years_range = list(range(datetime.now().year, datetime.now().year + years + 1))
        
        # 不導入技術的成本
        baseline = [base_cost * (1 + growth_rate/100) ** i for i in range(years + 1)]
        
        # 導入技術後的成本
        with_tech = [base_cost * (1 - tech_saving/100) * (1 + growth_rate/100) ** i for i in range(years + 1)]
        
        # 累積節省
        cumulative_saving = [sum(baseline[:i+1]) - sum(with_tech[:i+1]) for i in range(years + 1)]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=years_range, y=baseline,
            name='不導入技術',
            line=dict(color='#e74c3c', dash='dash'),
            fill=None
        ))
        
        fig.add_trace(go.Scatter(
            x=years_range, y=with_tech,
            name='導入節能技術',
            line=dict(color='#2ecc71'),
            fill='tonexty',
            fillcolor='rgba(46, 204, 113, 0.2)'
        ))
        
        fig.update_layout(
            title=f'{years}年能源成本趨勢預測',
            xaxis_title='年份',
            yaxis_title='能源成本 (萬元)',
            height=400,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # 摘要指標
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            f"{years}年後年成本 (不導入)",
            f"{baseline[-1]:,.0f} 萬元",
            f"+{(baseline[-1]/base_cost - 1)*100:.0f}%"
        )
    
    with col2:
        st.metric(
            f"{years}年後年成本 (導入技術)",
            f"{with_tech[-1]:,.0f} 萬元",
            f"-{(1 - with_tech[-1]/baseline[-1])*100:.0f}%"
        )
    
    with col3:
        st.metric(
            f"{years}年累積節省",
            f"{cumulative_saving[-1]:,.0f} 萬元",
            "總效益"
        )

# ============ 自訂數據 ============
elif analysis_type == "自訂數據":
    st.markdown("### 📝 自訂風險數據分析")
    
    st.info("上傳您的風險數據 CSV 檔案，或使用範例數據進行分析")
    
    uploaded_file = st.file_uploader("上傳 CSV 檔案", type=['csv'])
    
    if uploaded_file is not None:
        custom_df = pd.read_csv(uploaded_file)
        st.dataframe(custom_df, use_container_width=True)
        
        # 自動偵測數值欄位
        numeric_cols = custom_df.select_dtypes(include=[np.number]).columns.tolist()
        
        if len(numeric_cols) >= 2:
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox("X 軸", numeric_cols)
            with col2:
                y_col = st.selectbox("Y 軸", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
            
            fig = px.scatter(custom_df, x=x_col, y=y_col, title=f'{y_col} vs {x_col}')
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.markdown("#### 使用範例數據")
        
        if st.button("載入範例風險數據"):
            st.dataframe(risk_df, use_container_width=True)
            
            st.download_button(
                "下載範例 CSV",
                risk_df.to_csv(index=False, encoding='utf-8-sig'),
                "tcfd_risk_sample.csv",
                "text/csv"
            )

# ============ 頁腳 ============
st.divider()
st.caption(f"📊 數據分析工具 | 最後更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}")


