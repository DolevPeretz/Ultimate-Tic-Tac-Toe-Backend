from typing import List, Optional
from src.ultimate_tic_tac_toe.domain.enums.current_player import Current_Player


class MiniBoard:
    def __init__(self, row: int, col: int, currentPlayer: Current_Player):
        self.mainBoard: List[List[Current_Player | None]] = [[None for _ in range(3)] for _ in range(3)]
        self.currentPlayer = currentPlayer
        self.winner = None

    def make_move(self, row: int, col: int) -> dict:
        if self.mainBoard[row][col] is None:
            self.mainBoard[row][col] = self.currentPlayer
            self.currentPlayer = "O" if self.currentPlayer == "X" else "X"
            return {"message": "Move completed", "new_board": self.mainBoard, "current_player": self.currentPlayer}
        else:
            return {"message": "Invalid move, square is already occupied."}

    def check_winner(self) -> Optional[str]:
        for row in self.mainBoard:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return row[0]
        for col in range(3):
            if self.mainBoard[0][col] == self.mainBoard[1][col] == self.mainBoard[2][col] and self.mainBoard[0][
                col] is not None:
                return self.mainBoard[0][col]
        if self.mainBoard[0][0] == self.mainBoard[1][1] == self.mainBoard[2][2] and self.mainBoard[0][0] is not None:
            return self.mainBoard[0][0]
        if self.mainBoard[0][2] == self.mainBoard[1][1] == self.mainBoard[2][0] and self.mainBoard[0][2] is not None:
            return self.mainBoard[0][2]
        return None
