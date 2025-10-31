import streamlit as st
from summarization import summarize_all_articles

st.set_page_config(page_title="AI News Summarizer", layout="wide")

st.title("🤖 AI-Powered Drone & Tech News Summarizer")
st.write("This app discovers the latest industry news, summarizes it with AI, and formats it for social media sharing.")

# --- Sidebar for customization ---
st.sidebar.header("Settings")
topics = [
    "Drone Technology",
    "AI Innovations",
    "UAV & Defense",
    "Renewable Energy",
    "Cybersecurity",
    "Space Tech"
]

selected_topic = st.sidebar.selectbox("Choose a news topic:", topics)
num_articles = st.sidebar.slider("Number of articles to summarize:", 1, 5, 3)
refresh = st.sidebar.button("🔄 Refresh News")

# --- Main content area ---
if st.button("📰 Fetch Latest Summaries") or refresh:
    with st.spinner("Fetching latest news and generating summaries..."):
        results = summarize_all_articles(selected_topic, num_articles)

        if not results:
            st.error("⚠️ No news articles found. Try again later or change topic.")
        else:
            for article in results:
                st.subheader(article["title"])
                image_url = article.get("image")
                if image_url and isinstance(image_url, str) and image_url.strip():
                    try:
                        st.image(image_url, use_container_width=True)
                    except Exception:
                        st.write("⚠️ Unable to load image.")
                else:
                    st.write("📰 No image available for this article.")
                
                st.write(article["summary"])
                if "hashtags" in article and article["hashtags"]:
                    st.markdown(f"**Hashtags:** {article['hashtags']}")
                st.markdown(f"🔗 [Read Full Article]({article['link']})")
                st.markdown("---")
else:
    st.info("👆 Select a topic and click 'Fetch Latest Summaries' to begin.")
