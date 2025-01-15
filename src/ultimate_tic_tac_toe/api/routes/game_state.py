from fastapi import APIRouter
from src.ultimate_tic_tac_toe.api.models.game_session_creation_request_api_model import \
    GameSessionCreationRequestApiModel
from src.ultimate_tic_tac_toe.api.models.Game_State import GameStateApiModel
from src.ultimate_tic_tac_toe.domain.entities.MainBoardModel import MainBoard

game_state_router = APIRouter(prefix="/gameState")

@game_state_router.post("")
async def create_game_session(creation_request: GameSessionCreationRequestApiModel) -> GameStateApiModel:
    raise NotImplementedError()


@game_state_router.get("/{game_states_id}")
async def list_game_states(game_states_id: str) -> GameStateApiModel:
    raise NotImplementedError()

@game_state_router.delete("/{game_states_id}")
async def delete_game_board(game_states_id: str):
    MainBoard.delete_main_board_by_id(game_states_id)
    raise NotImplementedError()

