# from src.ultimate_tic_tac_toe.domain.enums import current_player
#
# class UltimateTicTacToe:
#     def __init__(self):
#         self.board = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
#         self.current_player = "X"
#         self.winner = None
#
#     def print_board(self):
#         # הצגת הלוח הראשי 3x3, כשכל תא הוא לוח קטן של 3x3
#         for i in range(3):
#             for j in range(3):
#                 index = i * 3 + j
#                 print(f"MiniBoard {index + 1}:")
#                 self.board[index].print_board()
#
#     def make_move(self, layer, x, y):
#         if self.board[layer][x][y] is not None:
#             raise ValueError("מקום זה כבר תפוס!")
#         self.board[layer][x][y] = self.current_player
#         if self.check_winner():
#             self.winner = self.current_player
#         else:
#             self.current_player ="O" if self.current_player == "X" else "X"
#
#     def check_winner(self):
#         for layer in self.board:
#             for row in layer:
#                 if all(s == self.current_player for s in row):
#                     return True
#         for col in range(3):
#             for row in range(3):
#                 if all(self.board[layer][row][col] == self.current_player for layer in range(3)):
#                     return True
#         for diag in range(3):
#             if all(self.board[diag][diag][diag] == self.current_player for diag in range(3)):
#                 return True
#             if all(self.board[diag][diag][2 - diag] == self.current_player for diag in range(3)):
#                 return True
#         return False