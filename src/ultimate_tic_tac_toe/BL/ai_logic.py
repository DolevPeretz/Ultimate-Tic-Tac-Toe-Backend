class TicTacToeAI:
    def __init__(self, game):
        self.game = game
        self.current_player = "O"

    def evaluate(self, board):
        winner = self.game.check_winner()
        if winner == "X":
            return 10
        elif winner == "O":
            return -10
        else:
            return 0

    def get_possible_moves(self, board):

        moves = []
        for i in range(9):
            mini_board = board[i]
            for x in range(3):
                for y in range(3):
                    if mini_board.board[x][y] is None:
                        moves.append((i, x, y))
        return moves

    def evaluate_move(self, board, mini_board_index, x, y, player):

        self.game.board[mini_board_index].make_move(x, y, player)
        score = self.evaluate(board)
        self.game.board[mini_board_index].board[x][y] = None
        return score

    def best_move(self):

        best_move = None
        best_score = -float('inf')

        for i in range(9):
            for x in range(3):
                for y in range(3):
                    if self.game.board[i].board[x][y] is None:
                        score = self.evaluate_move(self.game.board, i, x, y, self.current_player)
                        if score > best_score:
                            best_score = score
                            best_move = (i, x, y)

        return best_move



# class TicTacToeAI:
#     def __init__(self, game):
#         self.game = game  # גישה למשחק כדי לגשת ללוח ולבצע מהלכים
#         self.player = "O"  # המחשב תמיד יהיה "O"
#         self.opponent = "X"  # היריב תמיד יהיה "X"
#
#     def best_move(self):
#         """
#         מחזיר את המהלך הטוב ביותר עבור המחשב.
#         """
#         best_val = -float('inf')
#         best_move = None
#         for i in range(9):
#             if self.game.board[i].check_winner() is None:  # אם הלוח הקטן פנוי
#                 for x in range(3):
#                     for y in range(3):
#                         if self.game.board[i].board[x][y] is None:  # אם המקום פנוי
#                             self.game.board[i].make_move(x, y, self.player)  # המחשב מבצע מהלך
#                             move_val = self.minimax(self.game.board, 0, False)
#                             self.game.board[i].board[x][y] = None  # מחזיר את הלוח למצבו הקודם
#                             if move_val > best_val:
#                                 best_val = move_val
#                                 best_move = (i, x, y)
#         return best_move
#
#     def minimax(self, board, depth, is_maximizing):
#
#         stack = [(board, depth, is_maximizing)]
#         best_val = -float('inf') if is_maximizing else float('inf')
#
#         while stack:
#             curr_board, curr_depth, is_maximizing_player = stack.pop()
#
#             if self.check_game_over(curr_board):
#                 return self.evaluate(curr_board)
#
#             if is_maximizing_player:
#                 best = -float('inf')
#                 found_move = False
#                 for i in range(9):
#                     if self.game.board[i].check_winner() is None:  # אם הלוח הקטן פנוי
#                         for x in range(3):
#                             for y in range(3):
#                                 if curr_board[i].board[x][y] is None:  # אם המקום פנוי
#                                     curr_board[i].make_move(x, y, self.player)
#                                     best = max(best, self.minimax(curr_board, curr_depth + 1, False))
#                                     curr_board[i].board[x][y] = None  # מחזיר את הלוח למצבו הקודם
#                                     found_move = True
#                 if not found_move:  # אם לא נמצא שום מהלך תקין
#                     best= 0  # תיקו
#                 print(best)
#                 return best
#             else:
#                 best = float('inf')
#                 found_move = False
#                 for i in range(9):
#                     if self.game.board[i].check_winner() is None:  # אם הלוח הקטן פנוי
#                         for x in range(3):
#                             for y in range(3):
#                                 if curr_board[i].board[x][y] is None:  # אם המקום פנוי
#                                     curr_board[i].make_move(x, y, self.opponent)
#                                     best = min(best, self.minimax(curr_board, curr_depth + 1, True))
#                                     curr_board[i].board[x][y] = None  # מחזיר את הלוח למצבו הקודם
#                                     found_move = True
#                 if not found_move:  # אם לא נמצא שום מהלך תקין
#                     return 0  # תיקו
#                 return best
#
#     def check_game_over(self, board):
#         """
#         בודק אם המשחק הגיע לסיום.
#         """
#         # בדוק אם יש מנצח או אם כל הלוחות מלאים.
#         for i in range(9):
#             if board[i].check_winner() is not None:  # אם יש מנצח בלוח הקטן
#                 return True
#         return False
#
#     def evaluate(self, board):
#         """
#         פונקציה להעריך את המצב של המשחק על פי המנצח.
#         """
#         for i in range(9):
#             if board[i].check_winner() == self.player:  # אם המחשב מנצח בלוח קטן
#                 return 10
#             elif board[i].check_winner() == self.opponent:  # אם היריב מנצח בלוח קטן
#                 return -10
#         return 0  # תיקו



# class TicTacToeAI:
#     def __init__(self, game):
#         self.game = game
#         self.current_player = "O"  # המחשב הוא תמיד O
#         self.opponent = "X"  # השחקן הוא X
#
#     def evaluate(self, board):
#         """
#         פונקציה זו בודקת אם יש מנצח (בהתאם לתנאים שונים שיכולים להיות לך)
#         """
#         winner = self.game.check_winner()
#         if winner == "X":
#             return 10  # ניצחון לשחקן
#         elif winner == "O":
#             return -10  # ניצחון למחשב
#         else:
#             return 0  # תיקו
#
#     def get_possible_moves(self, board):
#         """
#         מחזירה את כל המקומות הפנויים בלוח
#         """
#         moves = []
#         for i in range(9):  # עבור כל המיני-לוחות
#             mini_board = board[i]
#             for x in range(3):  # עבור כל השורות במיני-לוח
#                 for y in range(3):  # עבור כל העמודות במיני-לוח
#                     if mini_board.board[x][y] is None:  # אם המקום פנוי
#                         moves.append((i, x, y))  # הוספת המיקום הפנוי
#         return moves
#
#     def evaluate_move(self, board, mini_board_index, x, y, player):
#         """
#         פונקציה זו בודקת את המהלך שנעשה על הלוח מבלי לשנות את המצב.
#         """
#         # דימוי המהלך
#         self.game.board[mini_board_index].make_move(x, y, player)  # המחשב עושה את המהלך
#         score = self.evaluate(board)  # מחשבים את הציון לאחר המהלך
#         self.game.board[mini_board_index].board[x][y] = None  # מחזירים את הלוח למצבו הקודם
#         return score
#
#     def best_move(self):
#         """
#         מחשבת את המהלך הטוב ביותר עבור המחשב ומחזירה את המיקום בלוח.
#         """
#         best_move = None
#         best_score = -float('inf')
#
#         # קודם כל נבדוק אם יש אפשרות לנצח
#         for i in range(9):
#             for x in range(3):
#                 for y in range(3):
#                     if self.game.board[i].board[x][y] is None:  # אם המקום פנוי
#                         self.game.board[i].make_move(x, y, self.current_player)  # המחשב עושה את המהלך
#                         if self.game.check_winner():  # אם המחשב ניצח
#                             self.game.board[i].board[x][y] = None  # מחזירים את המהלך למצבו הקודם
#                             return i, x, y  # אם ניצחנו מחזירים את המיקום
#
#         # אם לא מצאנו מהלך לניצחון, נבדוק אם השחקן יכול לנצח ונחסום אותו
#         block_move = self.block_opponent_win(self.game.board)
#         if block_move:
#             return block_move  # נחסום את השחקן אם הוא יכול לנצח
#
#         # אם אין לנצח או לחסום, נבחר את המהלך הטוב ביותר באמצעות מינימקס
#         for i in range(9):
#             for x in range(3):
#                 for y in range(3):
#                     if self.game.board[i].board[x][y] is None:  # אם המקום פנוי
#                         score = self.evaluate_move(self.game.board, i, x, y, self.current_player)  # מחשבים את הציון של המהלך
#                         if score > best_score:  # אם הציון טוב יותר מהציון הקודם
#                             best_score = score
#                             best_move = (i, x, y)  # עדכון המהלך הטוב ביותר
#
#         # מחזירים את המהלך הטוב ביותר (מיני-לוח, שורה, עמודה)
#         return best_move
#
#     def block_opponent_win(self, board):
#         """
#         בודקת אם יש אפשרות לשחקן לנצח במהלך הבא ומחסום אותו
#         """
#         for i in range(9):  # עבור כל המיני-לוחות
#             for x in range(3):  # עבור כל השורות במיני-לוח
#                 for y in range(3):  # עבור כל העמודות במיני-לוח
#                     if self.game.board[i].board[x][y] is None:
#                         self.game.board[i].make_move(x, y, self.opponent)  # השחקן עושה את המהלך
#                         if self.game.check_winner():  # אם השחקן מנצח
#                             self.game.board[i].board[x][y] = None  # מחזירים את המהלך למצבו הקודם
#                             return i, x, y  # מחזירים את המהלך שיבטיח את ההגנה
#                         self.game.board[i].board[x][y] = None  # אם לא מנצח מחזירים את המהלך למצבו הקודם
#         return None  # אם אין איום, לא חסמנו
