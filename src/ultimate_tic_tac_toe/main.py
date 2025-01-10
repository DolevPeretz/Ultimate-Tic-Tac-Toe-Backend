import uvicorn
from fastapi import FastAPI
from src.ultimate_tic_tac_toe.api.routes import game_sessions_router

app = FastAPI()

app.include_router(game_sessions_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
