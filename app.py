
import streamlit as st
import random

st.set_page_config(
    page_title="YouTube Creator Studio",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 YouTube AI Creator Studio")
st.caption("Your personal YouTube content assistant")

st.sidebar.title("Dashboard")
page = st.sidebar.radio(
    "Choose a tool",
    ["Home", "Video Ideas", "Title Generator", "Hashtag Generator"]
)

if page == "Home":
    st.header("Welcome to your Creator Studio!")
    st.write("Create better YouTube content with your assistant.")
    st.info("Choose a tool from the sidebar to get started.")

elif page == "Video Ideas":
    st.header("💡 Video Idea Generator")
    niche = st.text_input("Enter your video niche", "Anime")
    if st.button("Generate Ideas"):
        ideas = [
            f"Top 10 surprising facts about {niche}",
            f"Things you didn't know about {niche}",
            f"The biggest mystery in {niche}",
            f"5 mistakes beginners make in {niche}",
            f"What happens when {niche} meets the future?"
        ]
        for idea in ideas:
            st.write("🔥 " + idea)

elif page == "Title Generator":
    st.header("📝 Title Generator")
    topic = st.text_input("Enter your video topic")
    if st.button("Generate Titles"):
        if topic.strip():
            titles = [
                f"You Won't Believe This About {topic}!",
                f"5 Amazing Facts About {topic}",
                f"The Truth About {topic}",
                f"Everything You Need to Know About {topic}",
                f"This Changes Everything About {topic}"
            ]
            for title in titles:
                st.write("🚀 " + title)
        else:
            st.warning("Please enter a topic.")

elif page == "Hashtag Generator":
    st.header("#️⃣ Hashtag Generator")
    topic = st.text_input("Enter your topic")
    if st.button("Generate Hashtags"):
        if topic.strip():
            clean = topic.replace(" ", "")
            tags = [
                "#" + clean,
                "#YouTube",
                "#Shorts",
                "#Trending",
                "#Creator",
                "#ViralVideo"
            ]
            st.code(" ".join(tags))
        else:
            st.warning("Please enter a topic.")

st.divider()
st.caption("YouTube Creator Studio | Version 1.0")
