from typing import List, Tuple
from src.ultimate_tic_tac_toe.BL.mini_board import MiniBoard
from src.ultimate_tic_tac_toe.domain.enums.current_player import Current_Player


class MainBoard:
    def __init__(self):
        self.board: List[MiniBoard] = [MiniBoard() for _ in range(9)]  # הגדרת טיפוס ברור לרשימה של MiniBoard
        self.current_player = Current_Player.X
        self.winner = None

    def print_board(self):
        for i in range(3):
            row: List[MiniBoard] = []  # הצהרה ברורה על סוג המשתנה של row
            for j in range(3):
                index = i * 3 + j
                row.append(self.board[index])  # הוספת כל MiniBoard לשורה
            self.print_mini_boards(row)

    def print_mini_boards(self, row: List[MiniBoard]) -> None:  # הגדרת טיפוס ברור
        for i in range(3):
            print(f"{row[0].board[i]} | {row[1].board[i]} | {row[2].board[i]}")
        print("-" * 9)

    def make_move(self, mini_board_index: int, x: int, y: int) -> bool:
        mini_board = self.board[mini_board_index]
        if mini_board.make_move(x, y, self.current_player):
            return True
        return False

    def get_possible_moves(self) -> List[Tuple[int, int, int]]:
        moves: List[Tuple[int, int, int]] = [] 
        for i in range(9):
            mini_board = self.board[i]
            for x in range(3):
                for y in range(3):
                    if mini_board.board[x][y] is "None":
                        moves.append((i, x, y))
        return moves

    def score(self, depth: int) -> int:
        if self.is_over():
            return 10 - depth  
        return 0

    def minimax(self, depth: int, is_maximizing_player: bool) -> int:
        if self.is_over():
            return self.score(depth)

        depth += 1
        scores: List[int] = []  # רשימה לאחסון ציונים
        moves: List[Tuple[int, int, int]] = []  # רשימה לאחסון מהלכים אפשריים

        for move in self.get_possible_moves():
            mini_board_index, x, y = move
            self.make_move(mini_board_index, x, y)
            score = self.minimax(depth + 1, False)
            self.board[mini_board_index].board[x][y] = "None"  
            scores.append(score)
            moves.append(move)

        if is_maximizing_player:
            max_score_index = scores.index(max(scores))
            return scores[max_score_index]
        else:
            min_score_index = scores.index(min(scores))
            return scores[min_score_index]

    def best_move(self) -> Tuple[int, int, int] | None:
        best_move = None
        best_score = -float('inf')

        for move in self.get_possible_moves():
            mini_board_index, x, y = move
            self.make_move(mini_board_index, x, y)
            score = self.minimax(0, False)
            self.board[mini_board_index].board[x][y] = "None"  

            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def StateGame(self) -> None:
        while not self.winner:
            self.print_board()
            try:
                if self.current_player == Current_Player.X:
                    mini_board_index = int(input(f"Player {self.current_player}, choose MiniBoard (1-9): ")) - 1
                    if mini_board_index < 0 or mini_board_index > 8:
                        raise ValueError("The number must be between 1 and 9.")
                    x = int(input(f"Player {self.current_player}, insert row (0-2): "))
                    y = int(input(f"Player {self.current_player}, insert column (0-2): "))
                else:  
                    print("Computer's Turn:")
                    move = self.best_move()
                    print(move)
                    mini_board_index, x, y = move
                    print(f"Computer chose: MiniBoard {mini_board_index + 1}, Row {x}, Column {y}")

                if self.make_move(mini_board_index, x, y):
                    self.print_board()
                    if self.check_winner(self.current_player):
                        print(f"Player {self.current_player} wins the game!")
                        self.winner = self.current_player
                        break

                self.current_player = Current_Player.O if self.current_player == Current_Player.X else Current_Player.X

            except ValueError as e:
                print(e)
                continue

        print("The game is over")

    def check_winner(self, player: Current_Player) -> bool:
        for i in range(3):
            if self.board[i * 3].check_winner(player) and self.board[i * 3 + 1].check_winner(player) and self.board[
                i * 3 + 2].check_winner(player):
                return True

        for i in range(3):
            if self.board[i].check_winner(player) and self.board[i + 3].check_winner(player) and self.board[
                i + 6].check_winner(player):
                return True

        if self.board[0].check_winner(player) and self.board[4].check_winner(player) and self.board[8].check_winner(
                player):
            return True
        if self.board[2].check_winner(player) and self.board[4].check_winner(player) and self.board[6].check_winner(player):
            return True
        return False

    def is_over(self) -> bool:
        for mini_board in self.board:
            for row in mini_board.board:
                if "None" in row:
                    return False
        return True
