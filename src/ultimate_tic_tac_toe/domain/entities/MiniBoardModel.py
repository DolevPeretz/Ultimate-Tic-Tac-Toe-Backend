from typing import List
from src.ultimate_tic_tac_toe.domain.enums.current_player import Current_Player


class MiniBoard:
    def __init__(self, row: int, col: int, currentPlayer: Current_Player):
        self.mainBoard: List[List[Current_Player | None]] = [[None for _ in range(3)] for _ in range(3)]
        self.currentPlayer = currentPlayer
        self.winner = None


