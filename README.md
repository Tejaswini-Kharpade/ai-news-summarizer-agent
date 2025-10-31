<h1 align="center">🤖 AI News Summarizer Agent</h1>

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=for-the-badge&logo=openai&logoColor=white)
![NewsAPI](https://img.shields.io/badge/NewsAPI-008080?style=for-the-badge&logoColor=white)
![Visual Studio](https://img.shields.io/badge/Visual_Studio-5C2D91?style=for-the-badge&logo=visual%20studio&logoColor=white)

</div>

The **AI News Summarizer Agent** automatically fetches the latest tech and industry news, summarizes it using OpenAI’s API, and formats it into social-media-ready content via a sleek Streamlit interface.

---

## 🚀 Features

- **🔍 News Discovery**  
  Fetches the latest articles using [NewsAPI](https://newsapi.org/) for trending topics such as AI, Drone Tech, Cybersecurity, and more.

- **🧠 AI Summarization**  
  Uses the OpenAI API to generate concise and engaging summaries for each article.

- **🏷️ Hashtag Generation**  
  Automatically produces relevant hashtags for social media posts.

- **💡 Streamlit Interface**  
  Simple and interactive web app for viewing summaries, images, and links.

- **⚙️ Customizable Settings**  
  Choose your topic, number of articles, and refresh news anytime.

---

## 🛠️ Tech Stack

| Component | Technology Used |
|------------|----------------|
| Programming Language | Python |
| News Fetching | NewsAPI |
| AI Summarization | OpenAI GPT API |
| Frontend | Streamlit |
| Environment Variables | Python-dotenv |

---

## 📦 Installation & Setup

1️⃣ Clone the Repository
<div>
<pre style="font-size: 1.2em;">
git clone https://github.com/<your-username>/ai-news-summarizer-agent.git
cd ai-news-summarizer-agent
  
</pre>
</div>


2️⃣ Create a Virtual Environment
<div>
<pre style="font-size: 1.2em;">
python -m venv venv
venv\Scripts\activate
  
</pre>
</div>


3️⃣ Install Dependencies
<div>
<pre style="font-size: 1.2em;">
pip install -r requirements.txt
  
</pre>
</div>


4️⃣ Set Up API Keys

Create a file named .env in your project root directory:
<div>
<pre style="font-size: 1.2em;">
OPENAI_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_news_api_key_here
  
</pre>
</div>


▶️ Run the Application
<div>
<pre style="font-size: 1.2em;">
streamlit run app.py
  
</pre>
</div>


Then open your browser and go to:
👉 http://localhost:8501


⚙️ Requirements

-Python 3.9+
-Streamlit
-OpenAI
-Requests
-Python-dotenv

