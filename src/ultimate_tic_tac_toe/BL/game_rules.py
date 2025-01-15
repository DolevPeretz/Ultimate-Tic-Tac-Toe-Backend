# from src.ultimate_tic_tac_toe.BL.game_logic import UltimateTicTacToe
#
#
# class GameRules:
#     def __init__(self):
#         self.game_active = True
#
#     def check_game_over(self, game: UltimateTicTacToe):
#         if game.winner:
#             return f"ניצחון! השחקן {game.winner} ניצח!"
#         for row in game.board:
#             if "" in row:
#                 return False
#         return "תיקו!"
