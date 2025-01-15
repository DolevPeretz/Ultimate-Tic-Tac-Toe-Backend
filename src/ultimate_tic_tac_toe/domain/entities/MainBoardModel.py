from http.client import HTTPException
from src.ultimate_tic_tac_toe.domain.entities.MiniBoardModel import MiniBoard


class MainBoard:
    def __init__(self):
        self.mainBoard = [[MiniBoard(3, 3, "X") for _ in range(3)] for _ in range(3)]
        self.winner = None



