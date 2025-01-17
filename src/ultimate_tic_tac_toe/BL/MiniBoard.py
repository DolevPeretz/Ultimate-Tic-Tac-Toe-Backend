class MiniBoard:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(row)
        print()

    def make_move(self, x, y,current_player):
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise ValueError("Not in the range ")
        if self.board[x][y] is not None:
            raise ValueError("The place alredy taken")
        self.board[x][y] = current_player
        return True
        # if self.check_winner():
        #     return True
        # return False

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True
        return False