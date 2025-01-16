class TicTacToeAI:
    def __init__(self, game):
        self.game = game
        self.current_player = "O"  # המחשב הוא תמיד O
        self.opponent = "X"  # השחקן הוא X

    def evaluate(self, board):
        """
        פונקציה זו בודקת אם יש מנצח (בהתאם לתנאים שונים שיכולים להיות לך)
        """
        winner = self.game.check_winner()
        if winner == "X":
            return 10  # ניצחון לשחקן
        elif winner == "O":
            return -10  # ניצחון למחשב
        else:
            return 0  # תיקו

    def get_possible_moves(self, board):
        """
        מחזירה את כל המקומות הפנויים בלוח
        """
        moves = []
        for i in range(9):  # עבור כל המיני-לוחות
            mini_board = board[i]
            for x in range(3):  # עבור כל השורות במיני-לוח
                for y in range(3):  # עבור כל העמודות במיני-לוח
                    if mini_board.board[x][y] is None:  # אם המקום פנוי
                        moves.append((i, x, y))  # הוספת המיקום הפנוי
        return moves

    def evaluate_move(self, board, mini_board_index, x, y, player):
        """
        פונקציה זו בודקת את המהלך שנעשה על הלוח מבלי לשנות את המצב.
        """
        # דימוי המהלך
        self.game.board[mini_board_index].make_move(x, y, player)  # המחשב עושה את המהלך
        score = self.evaluate(board)  # מחשבים את הציון לאחר המהלך
        self.game.board[mini_board_index].board[x][y] = None  # מחזירים את הלוח למצבו הקודם
        return score

    def best_move(self):
        """
        מחשבת את המהלך הטוב ביותר עבור המחשב ומחזירה את המיקום בלוח.
        """
        best_move = None
        best_score = -float('inf')

        for i in range(9):
            for x in range(3):
                for y in range(3):
                    if self.game.board[i].board[x][y] is None:  # אם המקום פנוי
                        score = self.evaluate_move(self.game.board, i, x, y, self.current_player)  # מחשבים את הציון של המהלך
                        if score > best_score:  # אם הציון טוב יותר מהציון הקודם
                            best_score = score
                            best_move = (i, x, y)  # עדכון המהלך הטוב ביותר

        return best_move
