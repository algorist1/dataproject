# app.py
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 인기 관광지 Top 10 🇰🇷", layout="wide")

st.title("서울 인기 관광지 Top 10 — Folium으로 보기 🗺️")
st.markdown(
    "아래 지도는 외국인 관광객에게 인기 있는 서울의 대표 관광지 **Top 10**을 표시합니다. "
    "사이드바에서 장소를 선택/해제해 보세요."
)

# Top10 장소 데이터: 이름, 위도, 경도, 설명
attractions = [
    {
        "name": "Gyeongbokgung (경복궁)",
        "lat": 37.57577,
        "lon": 126.97359,
        "desc": "조선의 대표 고궁 — 한국 전통 궁궐을 체험해보세요."
    },
    {
        "name": "N Seoul Tower (N서울타워)",
        "lat": 37.55117,
        "lon": 126.988228,
        "desc": "서울을 한눈에 볼 수 있는 전망 명소."
    },
    {
        "name": "Myeongdong (명동)",
        "lat": 37.56268,
        "lon": 126.98474,
        "desc": "쇼핑·길거리음식의 메카 — 화장품 쇼핑으로 인기."
    },
    {
        "name": "Bukchon Hanok Village (북촌 한옥마을)",
        "lat": 37.58288,
        "lon": 126.98357,
        "desc": "한옥 골목 산책 — 전통가옥과 사진명소."
    },
    {
        "name": "Insadong (인사동)",
        "lat": 37.5744,
        "lon": 126.9850,
        "desc": "전통 공예품과 찻집이 많은 문화거리."
    },
    {
        "name": "Hongdae (홍대/홍익대 주변)",
        "lat": 37.55528,
        "lon": 126.92333,
        "desc": "젊음의 거리, 스트리트 공연과 카페·클럽이 활발."
    },
    {
        "name": "Gangnam (강남)",
        "lat": 37.517235,
        "lon": 127.047325,
        "desc": "트렌디한 쇼핑·식당·K-pop 문화의 중심지."
    },
    {
        "name": "Dongdaemun Market (동대문)",
        "lat": 37.56328,
        "lon": 126.99524,
        "desc": "패션·야시장 — 밤에도 활기찬 쇼핑타운."
    },
    {
        "name": "Lotte World Tower / Seoul Sky (롯데월드타워)",
        "lat": 37.511234,
        "lon": 127.09803,
        "desc": "초고층 전망대 'Seoul Sky' — 서울 전경 뷰 포인트."
    },
    {
        "name": "COEX / Starfield Library (코엑스/별마당도서관)",
        "lat": 37.5110,
        "lon": 127.0596,
        "desc": "대형쇼핑몰 + 인스타 감성 도서관 명소."
    }
]

# 기본 지도 중심: 서울 시청 근처를 적당히 센터로
m = folium.Map(location=[37.56, 126.98], zoom_start=12)

# 사이드바: 체크박스로 장소 선택
st.sidebar.header("지도에 표시할 장소 선택")
names = [a["name"] for a in attractions]
selected = st.sidebar.multiselect("장소 선택 (초기값: 전체)", names, default=names)

# 마커 추가
for a in attractions:
    if a["name"] in selected:
        popup_html = f"<b>{a['name']}</b><br>{a['desc']}"
        folium.Marker(
            location=[a["lat"], a["lon"]],
            popup=popup_html,
            tooltip=a["name"],
            icon=folium.Icon(icon="info-sign")
        ).add_to(m)

# 지도 표시 (streamlit-folium 사용)
st.subheader("지도")
st_folium(m, width="100%", height=650)

# 우측/하단에 장소 목록 요약
st.markdown("---")
st.subheader("Top 10 장소 요약")
for i, a in enumerate(attractions, start=1):
    st.markdown(f"**{i}. {a['name']}** — {a['desc']}  \n위도: `{a['lat']}`, 경도: `{a['lon']}`")

st.markdown("---")
st.caption("Top10 선정 근거: Tripadvisor·VisitSeoul·Klook 등 주요 관광 가이드/플랫폼의 상위 목록을 종합했습니다. (출처 표기 포함)")

# 출처(간단)
with st.expander("출처 보기 (원문 페이지들)"):
    st.write("- Tripadvisor / Seoul top attractions · (예시) 인기 명소 목록 확인. ")
    st.write("- VisitSeoul (서울시 관광 공식) · 주요 명소 안내. ")
    st.write("- Klook / KoreaToDo 등 여행 가이드들(종합 상위권 반영).")
    st.write("※ 각 출처에서 제시하는 '순위'는 데이터/기준별로 다를 수 있습니다.")
