from fastapi import FastAPI
from .scraper import scraper
from fastapi import Query

app = FastAPI()

@app.get("/")
def root(date: int = Query(..., description="Date"), city: str = Query(..., description="City name"), region: str = Query(..., description="Region name")):
    url = f"https://www.ipma.pt/pt/otempo/prev.localidade.hora/#{city}&{region}"
    return scraper(url, date)