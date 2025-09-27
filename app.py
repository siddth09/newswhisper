from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import feedparser
import urllib.parse
import os

app = FastAPI(title="NewsWhisper")

# Mount static files at /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at root
@app.get("/")
def root():
    index_path = os.path.join("static", "index.html")
    return FileResponse(index_path)

@app.get("/search")
def search(query: str = Query(..., min_length=1)):
    q = query.strip()
    if not q:
        return JSONResponse(status_code=400, content={"detail": "empty query"})

    q_enc = urllib.parse.quote_plus(q)
    rss_url = f"https://news.google.com/rss/search?q={q_enc}&hl=en-US&gl=US&ceid=US:en"

    feed = feedparser.parse(rss_url)
    results = []
    for entry in feed.entries[:8]:
        results.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "snippet": entry.get("summary", "")
        })

    return JSONResponse(content={"query": q, "results": results})
