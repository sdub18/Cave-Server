from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

URL = 'https://www.nhl.com/gamecenter/pit-vs-bos/2021/01/26/2020020093#game=2020020093,game_state=live'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Basic route to make sure the server is working
@app.get("/")
async def root():
    return {"message": "Welcome to the Cave endpoint"}

# MARK: NFL ROUTES

# Route to web scrape for all information related to the current state of a game
@app.get("/nfl/game")
async def getCurrGameStatus():
    #<span class="period period--total">1</span>
    results = soup.find(id='period period--total')
    print(results.prettify())
    return "Success"