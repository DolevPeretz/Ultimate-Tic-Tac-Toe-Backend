
# from src.ultimate_tic_tac_toe.api.routes import game_sessions_routes
#
# app = FastAPI()
#
# app.include_router(game_sessions_routes)
import uvicorn
from fastapi import FastAPI
from src.ultimate_tic_tac_toe.api.routes.game_sessions_routes import game_sessions_router
from src.ultimate_tic_tac_toe.api.routes.game_state import game_state_router

app = FastAPI()

app.include_router(game_sessions_router, prefix="/gameSessions")
# app.include_router(game_state_router, prefix="/gameState")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)
