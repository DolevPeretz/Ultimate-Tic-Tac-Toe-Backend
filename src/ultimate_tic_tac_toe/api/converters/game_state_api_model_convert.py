from src.ultimate_tic_tac_toe.api.models.Game_State import GameStateApiModel  # נניח שזה המודל הפנימי שלך

class GameStateApi:

    @staticmethod
    def to_api_model(game_id: int) -> GameStateApiModel:
        game_state = GameStateApiModel.get_by_id(game_id)
        return GameStateApiModel(
            mainBoard=game_state.mainBoard,
            currentplayer=game_state.currentplayer
        )

    # @staticmethod
    # def from_api_model(game_id: int, updated_state: GameStateApiModel) -> GameStateApiModel:
    #     game_state = GameStateApiModel.get_by_id(game_id)
    #     game_state.update_state(updated_state)
    #     game_state.save()
    #     return GameStateApiModel(
    #         game_id=game_state.game_id,
    #         current_player=game_state.current_player,
    #         board=game_state.board,
    #         is_reset=game_state.is_reset,
    #         winner=game_state.winner,
    #         history=game_state.history
    #     )
