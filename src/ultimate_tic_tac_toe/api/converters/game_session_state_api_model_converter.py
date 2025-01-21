from src.ultimate_tic_tac_toe.api.models.game_state_api_model import GameStateApiModel
class GameStateApi:

    @staticmethod
    def to_api_model(game_id: int) -> GameStateApiModel:
        game_session_state = GameStateApiModel.get_by_id(game_id)
        return GameStateApiModel(
            id=game_session_state.id,
            mainBoard=game_session_state.mainBoard,
            currentplayer=game_session_state.currentplayer
        )

    @staticmethod
    def from_api_model(game_id: int) -> GameStateApiModel:
        game_state_api = GameStateApiModel.get_by_id(game_id)
        return GameStateApiModel(
            id=game_state_api.id,
            mainBoard=game_state_api.mainBoard,
            currentplayer=game_state_api.currentplayer
        )


