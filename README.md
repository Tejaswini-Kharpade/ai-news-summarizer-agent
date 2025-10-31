# AI News Summarizer Agent

### Objective
This project automates the discovery, summarization, and formatting of the latest industry news using AI tools and APIs.  
It gathers recent news articles based on selected keywords, summarizes them with OpenAI, and displays social-media-ready outputs through a Streamlit web app.



## Features

1. **News Discovery**
   - Fetches top 3–5 latest articles using the [NewsAPI](https://newsapi.org/).
   - Supports topics like Drone Technology, UAV, AI, and more.
   - Extracts title, publication date, link, and image.

2. **AI Summarization**
   - Uses the OpenAI API to summarize articles into short, engaging paragraphs.
   - Generates relevant hashtags and trending keywords automatically.

3. **Content Formatting**
   - Prepares social media–ready captions including:
     - Hook line
     - Summary
     - Hashtags
     - Article link

4. **Interactive Streamlit UI**
 - Users can select a topic and number of articles to summarize.  
 - Displays titles, summaries, hashtags, and article images neatly.


## Tech Stack

Component    Technology Used 

| Programming Language | Python |
| News Fetching | NewsAPI |
| AI Summarization | OpenAI GPT API |
| Frontend | Streamlit |
| Environment Variables | Python-dotenv |


## Setup Instructions

### 1. Clone or Download the Project
If you’re using GitHub:
```bash
git clone https://github.com/your-username/ai-news-summarizer.git
cd ai-news-summarizer


## Installation and Setup

1. Clone the repository

git clone https://github.com/yourusername/ai-news-summarizer.git
cd ai-news-summarizer

2. Create a virtual environment

python -m venv venv
source venv/Scripts/activate

3. Install dependencies

pip install -r requirements.txt

4. Set up your API keys

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_newsapi_key_here

5. Run the app

streamlit run app.py

6. Access the app

Open your browser and go to:
http://localhost:8501


## Requirements

Python 3.9+
Streamlit
openai
requests
python-dotenv