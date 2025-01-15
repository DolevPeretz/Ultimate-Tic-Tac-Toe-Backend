#
# class TicTacToeAI:
#     def __init__(self, game):
#         self.game = game
#         self.current_player = "O"
#
#     def minimax(self, board, depth, is_maximizing_player):
#
#         if self.game.check_winner():
#             if is_maximizing_player:
#                 return -1
#             else:
#                 return 1
#
#         if self.is_board_full(board):
#             return 0
#
#         if is_maximizing_player:
#             best_score = -float('inf')
#             for i in range(9):
#                 if board[i].board[x][y] is None:
#                     board[i].make_move(x, y, self.current_player)
#                     score = self.minimax(board, depth + 1, False)  # קריאה רקורסיבית
#                     board[i].board[x][y] = None  # לבטל את המהלך
#                     best_score = max(score, best_score)
#             return best_score
#         else:  # השחקן משחק את מהלך הכי טוב עבורו
#             best_score = float('inf')
#             for i in range(9):
#                 if board[i].board[x][y] is None:
#                     board[i].make_move(x, y, self.other_player())
#                     score = self.minimax(board, depth + 1, True)  # קריאה רקורסיבית
#                     board[i].board[x][y] = None  # לבטל את המהלך
#                     best_score = min(score, best_score)
#             return best_score
#
#     def best_move(self):
#
#         best_move = None
#         best_score = -float('inf')
#
#         for i in range(9):
#             for x in range(3):
#                 for y in range(3):
#                     if self.game.board[i].board[x][y] is None:
#                         self.game.board[i].make_move(x, y, self.current_player)
#                         score = self.minimax(self.game.board, 0, False)
#                         self.game.board[i].board[x][y] = None
#                         if score > best_score:
#                             best_score = score
#                             best_move = (i, x, y)
#         return best_move
#
#     def is_board_full(self, board):
#
#         for i in range(9):
#             for x in range(3):
#                 for y in range(3):
#                     if board[i].board[x][y] is None:
#                         return False
#         return True
#
#     def other_player(self):
#
#         return "X" if self.current_player == "O" else "O"
