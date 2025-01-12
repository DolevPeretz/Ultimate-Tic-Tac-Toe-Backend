from typing import List, Optional
from  MiniBoard import MiniBoard


class MainBoard:
    def __init__(self):
        self.mainBoard = [[MiniBoard(3, 3, "X") for _ in range(3)] for _ in range(3)]  # 9 לוחות מיני
        self.winner = None

    def make_move_main_board(self, mini_board_row: int, mini_board_col: int, row: int, col: int) -> dict:
        mini_board = self.mainBoard[mini_board_row][mini_board_col]
        result = mini_board.make_move(row, col)

        if result["message"] == "Move completed":
            self.history.append(mini_board.on_move)
            self.current_player = "O" if self.current_player == "X" else "X"
            winner = mini_board.check_winner()
            if winner:
                self.winner = winner
        return result

    def check_main_board_winner(self) -> Optional[str]:
        for row in self.mainBoard:
            for mini_board in row:
                winner = mini_board.check_winner()
                if winner:
                    return winner
        return None
