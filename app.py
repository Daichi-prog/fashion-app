import streamlit as st
import os

st.title("ビジネスカジュアル提案アプリ")

gender = st.selectbox("性別", ["男性", "女性"])
season = st.selectbox("季節", ["春", "夏", "秋", "冬"])
style = st.selectbox("スタイル", ["オフィスカジュアル", "ビジネスカジュアル"])

gender_map = {
    "男性": "men",
    "女性": "women"
}

season_map = {
    "春": "spring",
    "夏": "summer",
    "秋": "autumn",
    "冬": "winter"
}

style_map = {
    "オフィスカジュアル": "office",
    "ビジネスカジュアル": "business"
}

image_name = f"{season_map[season]}_{gender_map[gender]}_{style_map[style]}.jpg"

st.write("選択条件：", gender, season, style)

if os.path.exists(image_name):
    st.image(image_name, use_container_width=True)
else:
    st.warning(f"画像がまだありません：{image_name}")