
import streamlit as st
import datetime
import requests
from PIL import Image
from io import BytesIO

# 페이지 설정
st.set_page_config(page_title="🌸 BloomNote - 오늘의 경제 상태창", layout="centered")

# 📅 현재 날짜 & 요일
now = datetime.datetime.now()
korean_days = ["월", "화", "수", "목", "금", "토", "일"]
date_str = now.strftime(f"%Y년 %m월 %d일 ({korean_days[now.weekday()]}요일)")

# 🎀 둥근모 폰트 적용
st.markdown("""
<style>
@font-face {
  font-family: 'DungGeunMo';
  src: url('https://raw.githubusercontent.com/caleb25613/bloomnote/main/BloomNote_Font_DungGeunMo.ttf');

html, body, [class*="css"]  {
  font-family: 'DungGeunMo', sans-serif;
  background-color: #fff0f5;
  color: #4b2e2e;
}
</style>
""", unsafe_allow_html=True)

# 💖 상단 이미지 (게임 상태창 느낌)
st.image("https://i.ibb.co/QnRQRPt/gamestatus-bar.png", use_column_width=True)

st.title("🌸 BloomNote - 오늘의 경제 상태창")
st.markdown(f"**📆 {date_str} 기준 실시간 정보입니다!**")

# 📊 실시간 지수 데이터
st.markdown("---")
st.subheader("📈 주요 지수 현황")

index_data = {
    "S&P500": "https://query1.finance.yahoo.com/v8/finance/chart/^GSPC",
    "NASDAQ": "https://query1.finance.yahoo.com/v8/finance/chart/^IXIC",
    "DOW JONES": "https://query1.finance.yahoo.com/v8/finance/chart/^DJI"
}

def get_price(url):
    try:
        res = requests.get(url)
        json_data = res.json()
        price = json_data['chart']['result'][0]['meta']['regularMarketPrice']
        return price
    except:
        return "정보 없음"

cols = st.columns(3)
for i, (name, url) in enumerate(index_data.items()):
    with cols[i]:
        st.metric(label=name, value=f"{get_price(url)}")

# 📰 오늘의 경제 기사 (여성향 말투)
st.markdown("---")
st.subheader("📰 오늘의 경제 기사 💌")

news = """
🌷 *오늘은 미국의 소매판매 지표가 발표되었어요.*
생각보다 낮은 수치였지만, 그 안엔 숨은 긍정적 신호도 있었답니다. 🌸

핵심 소비지표는 전월보다 1.0% 증가했어요.
이 말은 우리 경제가 아직 따뜻한 숨결을 유지하고 있다는 신호일지도 몰라요. 💗

지금처럼 불확실한 시기일수록, 나만의 기준과 전략을 꼭 지켜주세요.
오늘도 현명한 투자자로 한 걸음 가까워지는 하루 되길 바랄게요. ☕
"""

st.info(news)

# 💾 저장 안내
st.markdown("""
---
💾 **BloomNote는 매일 아침 당신만을 위한 경제 메모를 전해드립니다.**
문의나 제안은 [GitHub](https://github.com/caleb25613/investment-reminder-app)에서 남겨주세요 ✨
""")
