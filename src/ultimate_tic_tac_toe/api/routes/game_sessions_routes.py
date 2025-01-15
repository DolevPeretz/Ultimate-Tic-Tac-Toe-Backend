import uuid
from fastapi import HTTPException, status
from datetime import datetime
from fastapi import APIRouter
from src.ultimate_tic_tac_toe.api.models.game_session_creation_request_api_model import \
    GameSessionCreationRequestApiModel
from src.ultimate_tic_tac_toe.api.models.game_session_metadata_api_model import GameSessionMetadataApiModel
from src.ultimate_tic_tac_toe.domain.enums.state_game import StateGame
game_sessions_router = APIRouter(prefix="/gameSessions")
game_sessions_dict={}


@game_sessions_router.post("")
async def create_game_session(creation_request: GameSessionCreationRequestApiModel) -> GameSessionMetadataApiModel:
    game_session_id = str(uuid.uuid4())
    game_session_name = str(uuid.uuid4())
    game_session_title = ""
    game_session_status = StateGame.in_progress
    game_session_difficulty = creation_request.difficultyLevel
    current_time = datetime.now()

    game_session = GameSessionMetadataApiModel(
        id=game_session_id,
        name=game_session_name,
        title=game_session_title,
        status=game_session_status,
        difficulty_level=game_session_difficulty,
        create_time=current_time,
        update_time=current_time
    )
    game_sessions_dict[game_session_id] = game_session
    return game_session


@game_sessions_router.get("")
async def list_game_sessions() -> list[GameSessionMetadataApiModel]:
    return list(game_sessions_dict.values())



@game_sessions_router.get("/{game_session_id}")
async def get_game_session(game_session_id: str) -> GameSessionMetadataApiModel:
    game_session = game_sessions_dict.get(game_session_id)
    if not game_session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game session with ID {game_session_id} not found"
        )
    return game_session




@game_sessions_router.delete("/{game_session_id}")
async def delete_game_session(game_session_id: str):
    game_session = game_sessions_dict.pop(game_session_id, None)
    if not game_session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game session with ID {game_session_id} not found"
        )
    return {"message": f"Game session with ID {game_session_id} has been deleted."}


