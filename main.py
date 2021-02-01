from fastapi import FastAPI

app = FastAPI()

# Basic route to make sure the server is working
@app.get("/")
async def root():
    return {"message": "Welcome to the Cave endpoint"}

# MARK: NBA ROUTES

# Route to retrieve all current games being played in the NBA League
@app.get("/nba/games")
async def getCurrGameStatus():
    return "F"