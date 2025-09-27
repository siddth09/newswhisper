# 🎙️ NewsWhisper

NewsWhisper is a **voice-powered Google News search tool**.  
It allows users to speak their search queries and get top news snippets instantly.

---

## Features
- Voice input (Start / Stop controls)
- Top news snippets fetched from Google News RSS
- Display title, link, published date, and snippet
- Lightweight, open-source, and easy to run locally or on GCP

---

## Tech Stack
- **Backend:** FastAPI
- **Frontend:** HTML + JS (Voice input)
- **RSS Parsing:** feedparser
- **Server:** Uvicorn
- **Hosting (Optional):** Google Cloud Run

---

## YouTube Demo

Watch the live demo of NewsWhisper here:  
[![NewsWhisper Demo](https://img.youtube.com/vi/heCAEsVVUws/0.jpg)](https://www.youtube.com/watch?v=heCAEsVVUws&feature=youtu.be)

Click the thumbnail or the link to see the demo in action.

---

## Setup Instructions (Local)
1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/newswhisper.git
cd newswhisper
````

2. Create virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

4. Open browser and visit:

```
http://localhost:8080/static/index.html
```

---

## Setup Instructions (GCP Cloud Run)

1. Ensure you have gcloud CLI installed and project configured.
2. Build Docker image:

```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/newswhisper
```

3. Deploy to Cloud Run:

```bash
gcloud run deploy newswhisper --image gcr.io/PROJECT_ID/newswhisper --platform managed --allow-unauthenticated --region REGION
```

---

## Notes

* Replace `PROJECT_ID` and `REGION` with your GCP project values.
* Replace `YOUR_VIDEO_ID` with your actual YouTube video ID.
* This project uses only free/open-source tools.

---

## License

MIT License
