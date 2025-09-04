from fastapi import FastAPI
from .scraper import scraper

app = FastAPI()

@app.get("/")
def root():
    return scraper("https://www.ipma.pt/pt/otempo/prev.localidade.hora/#Porto&Valongo")