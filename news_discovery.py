import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_latest_drone_news(topic="latest drone news", num_articles=3):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": num_articles,
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    for article in data.get("articles", []):
        articles.append({
            "title": article["title"],
            "link": article["url"],
            "publishedAt": article["publishedAt"],
            "image": article.get("urlToImage")
        })
    return articles

if __name__ == "__main__":
    for a in get_latest_drone_news():
        print(a)
