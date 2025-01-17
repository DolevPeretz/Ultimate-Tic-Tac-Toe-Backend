from src.ultimate_tic_tac_toe.BL.MiniBoard import MiniBoard
from src.ultimate_tic_tac_toe.BL.ai_logic import TicTacToeAI


class UltimateTicTacToe:
    def __init__(self):
        self.board = [MiniBoard() for _ in range(9)]
        self.current_player = "X"
        self.winner = None
        self.ai = TicTacToeAI(self)


    def print_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                index = i * 3 + j
                row.append(self.board[index])
            self.print_mini_boards(row)

    def print_mini_boards(self, row):
        for i in range(3):
            print(f"{row[0].board[i]} | {row[1].board[i]} | {row[2].board[i]}")
        print("-" * 9)

    def make_move(self, mini_board_index, x, y):

        while self.current_player == "X":
            mini_board = self.board[mini_board_index]
            if mini_board.make_move(x, y, self.current_player) :
                if mini_board.check_winner():
                    print(f"The Winer Of the Game {self.current_player} !")
                    if self.check_winner():
                        print(f" The Winer Of the Game  {self.current_player} !")
                        return True
                self.current_player = "O"
        while self.current_player == "O":
            move = self.ai.best_move()
            if move:
                mini_board_index, x, y = move
                mini_board = self.board[mini_board_index]
                if mini_board.make_move(x, y, "O"):
                    print(f"Computer Move {mini_board_index}, בשורה {x}, בעמודה {y}")
                    if self.check_winner():
                        print(f"The Winer Of the Game  {self.current_player} במשחק!")
                        return True
                    self.current_player = "X"

        return False

    def check_winner(self):
        for i in range(3):
            if self.board[i * 3].check_winner() and self.board[i * 3 + 1].check_winner() and self.board[
                i * 3 + 2].check_winner():
                print(f"Winer in the Row{self.current_player}  {i + 1}!")
                return True
        for i in range(3):
            if self.board[i].check_winner() and self.board[i + 3].check_winner() and self.board[i + 6].check_winner():
                print(f"Winer in the Colum {self.current_player}  {i + 1}!")
                return True

        if self.board[0].check_winner() and self.board[4].check_winner() and self.board[8].check_winner():
            print("Winer in the Diagonal")
            return True
        if self.board[2].check_winner() and self.board[4].check_winner() and self.board[6].check_winner():
            print("Winer in the Diagonal")
            return True

        return False
