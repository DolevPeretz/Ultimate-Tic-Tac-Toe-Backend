from src.ultimate_tic_tac_toe.BL.MiniBoard import MiniBoard


class UltimateTicTacToe:
    def __init__(self):
        self.board = [MiniBoard() for _ in range(9)]
        self.current_player = "X"
        self.winner = None

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
        mini_board = self.board[mini_board_index]
        if mini_board.make_move(x, y,self.current_player):
            print(f"ניצחון עבור {self.current_player} בלוח הקטן!")
            if self.check_winner():
                print(f"ניצחון עבור {self.current_player} במשחק!")
                return True
        self.current_player = "O" if self.current_player == "X" else "X"
        return False

    def check_winner(self):
        for i in range(3):
            if self.board[i * 3].check_winner() and self.board[i * 3 + 1].check_winner() and self.board[
                i * 3 + 2].check_winner():
                print(f"ניצחון עבור {self.current_player} בשורה {i + 1}!")
                return True

        for i in range(3):
            if self.board[i].check_winner() and self.board[i + 3].check_winner() and self.board[i + 6].check_winner():
                print(f"ניצחון עבור {self.current_player} בעמודה {i + 1}!")
                return True

        if self.board[0].check_winner() and self.board[4].check_winner() and self.board[8].check_winner():
            print("ניצחון באלכסון ראשי!")
            return True
        if self.board[2].check_winner() and self.board[4].check_winner() and self.board[6].check_winner():
            print("ניצחון באלכסון משני!")
            return True

        return False

