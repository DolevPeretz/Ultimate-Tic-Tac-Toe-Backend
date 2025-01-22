from fastapi import FastAPI
from src.ultimate_tic_tac_toe.api.routes.game_sessions_routes import game_sessions_router
app = FastAPI()
app.include_router(game_sessions_router, prefix="/gameSessions")
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)


# from src.ultimate_tic_tac_toe.BL.main_board import MainBoard
# 
# def play_game():
#     game = MainBoard()
# 
#     # הפעלת המשחק
#     game.StateGame()
# 
# if __name__ == "__main__":
#     play_game()











