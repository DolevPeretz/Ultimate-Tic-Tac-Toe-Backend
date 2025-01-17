from src.ultimate_tic_tac_toe.api.models.Game_State import GameStateApiModel

class GameStateApi:

    @staticmethod
    def to_api_model(game_id: int) -> GameStateApiModel:
        game_session_state = GameStateApiModel.get_by_id(game_id)
        return GameStateApiModel(
            mainBoard=game_session_state.mainBoard,
            currentplayer=game_session_state.currentplayer
        )

    @staticmethod
    def from_api_model(game_id: int) -> GameStateApiModel:
        game_session_api = GameStateApiModel.get_by_id(game_id)
        return GameStateApiModel(
            mainBoard=game_session_api.mainBoard,
            currentplayer=game_session_api.currentplayer
        )


