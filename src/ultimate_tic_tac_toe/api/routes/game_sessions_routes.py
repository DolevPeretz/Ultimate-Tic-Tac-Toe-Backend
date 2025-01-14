from http.client import HTTPException
from fastapi import APIRouter
from src.ultimate_tic_tac_toe.api.models.game_session_creation_request_api_model import \
    GameSessionCreationRequestApiModel
from src.ultimate_tic_tac_toe.api.models.game_session_metadata_api_model import GameSessionMetadataApiModel
from src.ultimate_tic_tac_toe.domain.entities.SessionGame import GameSession

game_sessions_router = APIRouter(prefix="/gameSessions")
game_sessions_db=[]


@game_sessions_router.post("")
async def create_game_session(creation_request: GameSessionCreationRequestApiModel) -> GameSessionMetadataApiModel:
    game_session = GameSession(difficultyLevel=creation_request.difficultyLevel)
    game_state = game_session.start_game()
    game_sessions_db.append(game_state)
    return game_state


@game_sessions_router.get("")
async def list_game_sessions() -> list[GameSessionMetadataApiModel]:
    return game_sessions_db


@game_sessions_router.get("/{game_session_id}")
async def get_game_session(game_session_id: str) -> GameSessionMetadataApiModel:
    game_session = GameSession.get_game_by_id(game_sessions_db, game_session_id)
    if game_session is None:
        raise NotImplementedError()
    return game_session


@game_sessions_router.delete("/{game_session_id}")
async def delete_game_session(game_session_id: str):
    result = GameSession.delete_game_by_id(game_sessions_db, game_session_id)
    if "not found" in result["message"]:
        raise HTTPException(status_code=404, detail=result["message"])
    return result

