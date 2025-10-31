import os
from openai import OpenAI
from dotenv import load_dotenv
from news_discovery import get_latest_drone_news

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_article(article):
    prompt = f"""
    Summarize this drone-related news article in 2–3 short paragraphs.
    Then list 3–5 relevant hashtags and trending keywords.

    Title: {article['title']}
    Link: {article['link']}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response.choices[0].message.content.strip()
    return summary


def summarize_all_articles(topic="latest drone news", num_articles=3):
    articles = get_latest_drone_news(topic, num_articles)
    summaries = []
    for article in articles:
        summary_text = summarize_article(article)
        summaries.append({
            "title": article["title"],
            "link": article["link"],
            "summary": summary_text
        })
    return summaries


if __name__ == "__main__":
    results = summarize_all_articles()
    for r in results:
        print("\n📰 Title:", r["title"])
        print(r["summary"])
        print("🔗 Link:", r["link"])
        print("-" * 80)
