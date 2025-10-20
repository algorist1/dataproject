import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(page_title="MBTI 국가별 분석", layout="wide")

# -----------------------------
# 데이터 로드
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# -----------------------------
# UI - 국가 선택
# -----------------------------
st.title("🌍 국가별 MBTI 유형 비율 분석")
st.markdown("**Plotly 기반 인터랙티브 시각화**")

countries = df["Country"].sort_values().unique()
selected_country = st.selectbox("국가를 선택하세요", countries, index=0)

# -----------------------------
# 데이터 필터링
# -----------------------------
country_data = df[df["Country"] == selected_country].iloc[0, 1:]  # 첫 행, MBTI 비율만
country_df = pd.DataFrame({
    "MBTI": country_data.index,
    "비율": country_data.values
}).sort_values("비율", ascending=False)

# -----------------------------
# 색상 설정
# -----------------------------
colors = ["#FF4B4B"] + [f"rgba(255,{150+i*5},{150+i*5},0.8)" for i in range(1, len(country_df))]

# -----------------------------
# Plotly 시각화
# -----------------------------
fig = px.bar(
    country_df,
    x="MBTI",
    y="비율",
    text="비율",
    color_discrete_sequence=colors
)

# 막대 색상 직접 설정
fig.update_traces(
    marker_color=[colors[i] for i in range(len(country_df))],
    texttemplate='%{text:.2%}',
    textposition='outside'
)

fig.update_layout(
    title=f"🇨🇺 {selected_country} MBTI 유형별 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    showlegend=False,
    title_x=0.5,
    plot_bgcolor="white",
    font=dict(size=14),
    margin=dict(t=80, b=60),
)

# -----------------------------
# 그래프 출력
# -----------------------------
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 하단 정보
# -----------------------------
st.markdown("---")
st.caption("📊 데이터 출처: MBTI 16유형 국가별 비율 데이터 (2025)")
