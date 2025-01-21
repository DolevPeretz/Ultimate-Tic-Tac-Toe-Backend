# from typing import List, Tuple
# from src.ultimate_tic_tac_toe.BL.main_board import MainBoard
# 
# 
# class ComputerLogicPlayer:
#     def __init__(self, player: str, opponent: str, game: MainBoard):
#         self.player = player
#         self.opponent = opponent
#         self.game = game
# 
#     def get_possible_moves(self, game: 'MainBoard') -> List[Tuple[int, int, int]]:
#         moves = []
#         for i in range(9):
#             mini_board = game.board[i]
#             for x in range(3):
#                 for y in range(3):
#                     if mini_board.board[x][y] is None:  # Check if the spot is available
#                         moves.append((i, x, y))
#         return moves
# 
#     def score(self, game: 'MainBoard', depth: int) -> int:
#         # Dummy score function, this should implement the actual evaluation logic
#         if game.is_over():
#             return 10 - depth  # Assuming maximizing player wins, modify as needed
#         return 0
# 
#     def evaluate_move(self, game: 'MainBoard', mini_board_index: int, x: int, y: int, player: str) -> int:
#         # Apply the move, evaluate, then undo
#         mini_board = game.board[mini_board_index]
#         mini_board.make_move(x, y, player)  # Make the move
#         score = self.score(game, 0)  # Evaluate the move
#         mini_board.board[x][y] = None  # Undo the move
#         return score
# 
#     def minimax(self, game: 'MainBoard', depth: int, is_maximizing_player: bool) -> int:
#         if game.is_over():
#             return self.score(game, depth)
# 
#         depth += 1
#         scores: List[int] = []  # List to store the scores
#         moves: List[Tuple[int, int, int]] = []  # List to store possible moves
# 
#         for move in self.get_possible_moves(game):
#             mini_board_index, x, y = move
#             score = self.evaluate_move(game, mini_board_index, x, y,
#                                        self.player if is_maximizing_player else self.opponent)
#             scores.append(score)
#             moves.append(move)
# 
#         if is_maximizing_player:
#             max_score_index = scores.index(max(scores))
#             return scores[max_score_index]
#         else:
#             min_score_index = scores.index(min(scores))
#             return scores[min_score_index]
