import streamlit as st

st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/monsterball.png"
)

st.title("streamlit 포켓몬 도감")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요!")

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

pokemon = {
    "name": "누오",
    "types": ["물", "땅"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp"
}

#st.subheader(pokemon["name"])
#st.image(pokemon["image_url"])
#st.subheader(' / '.join(pokemon["types"]))

with st.expander(label=f"{pokemon['name']}", expanded=True):
    st.image(pokemon["image_url"])
    emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
    st.subheader(" / ".join(emoji_types))