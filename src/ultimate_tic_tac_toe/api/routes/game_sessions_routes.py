from fastapi import APIRouter

from src.ultimate_tic_tac_toe.api.models.game_session_creation_request_api_model import \
    GameSessionCreationRequestApiModel
from src.ultimate_tic_tac_toe.api.models.game_session_metadata_api_model import GameSessionMetadataApiModel

game_sessions_router = APIRouter(prefix="/gameSessions")

@game_sessions_router.post("")
async def create_game_session(creation_request: GameSessionCreationRequestApiModel) -> GameSessionMetadataApiModel:
    # Here should be code to create a new game session object in the backend
    # then convert it to API model and return it
    raise NotImplementedError()

@game_sessions_router.get("")
async def list_game_sessions() -> list[GameSessionMetadataApiModel]:
    raise NotImplementedError()

@game_sessions_router.get("/{game_session_id}")
async def list_game_sessions(game_session_id: str) -> GameSessionMetadataApiModel:
    raise NotImplementedError()


