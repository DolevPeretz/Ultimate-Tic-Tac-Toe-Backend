
# from src.ultimate_tic_tac_toe.api.routes import game_sessions_routes
#
# app = FastAPI()
#
# app.include_router(game_sessions_routes)
import uvicorn
from fastapi import FastAPI

from src.ultimate_tic_tac_toe.BL.MainBoard import UltimateTicTacToe
from src.ultimate_tic_tac_toe.BL.ai_logic import TicTacToeAI
from src.ultimate_tic_tac_toe.api.routes.game_sessions_routes import game_sessions_router
from src.ultimate_tic_tac_toe.domain.entities.MainBoardModel import MainBoard
from src.ultimate_tic_tac_toe.domain.enums import current_player

app = FastAPI()

app.include_router(game_sessions_router, prefix="/gameSessions")
# app.include_router(game_state_router, prefix="/gameState")

def play_game():
    game = UltimateTicTacToe()

    while not game.winner:
        game.print_board()

        try:
            mini_board_index = int(input(f"שחקן {game.current_player}, בחר לוח קטן (1-9): ")) - 1
            if mini_board_index < 0 or mini_board_index > 8:
                raise ValueError("המספר חייב להיות בין 1 ל-9.")
            x = int(input(f"שחקן {game.current_player}, הכנס שורה (0-2): "))
            y = int(input(f"שחקן {game.current_player}, הכנס עמודה (0-2): "))

            if game.make_move(mini_board_index, x, y):
                game.print_board()
                print(f"שחקן {game.current_player} ניצח במשחק!")
                break
        except ValueError as e:
            print(e)
            continue

    print("המשחק הסתיים!")


if __name__ == "__main__":
    play_game()



# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=3000)
