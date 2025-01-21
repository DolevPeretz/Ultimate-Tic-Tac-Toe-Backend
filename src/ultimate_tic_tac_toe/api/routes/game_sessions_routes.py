import uuid
from fastapi import HTTPException, status
from datetime import datetime
from fastapi import APIRouter
from src.ultimate_tic_tac_toe.api.models.game_state_api_model import GameStateApiModel
from src.ultimate_tic_tac_toe.api.models.game_session_creation_request_api_model import \
    GameSessionCreationRequestApiModel
from src.ultimate_tic_tac_toe.api.models.game_session_metadata_api_model import GameSessionMetadataApiModel
from src.ultimate_tic_tac_toe.domain.enums.game_status import GameStatus
game_sessions_router = APIRouter(prefix="/gameSessions")
game_sessions_dict={}
from src.ultimate_tic_tac_toe.BL.services import Services

service=Services()

@game_sessions_router.post("")
async def create_game_session(creation_request: GameSessionCreationRequestApiModel) -> GameSessionMetadataApiModel:
    #לשאול את אלדר בנוגע ל-ID אם זה לא משהו שאמור להיווצר ב -DL אז למה הוא צריך להיות ב- MODEL?
    game_session_id = str(uuid.uuid4())
    game_session_name = str(uuid.uuid4())
    game_session_title = ""
    game_session_status = GameStatus.in_progress
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
    service.create_game_session_dl(game_session)
    return game_session


@game_sessions_router.get("")
async def list_game_sessions() -> list[GameSessionMetadataApiModel]:
    return service.list_game_sessions()



@game_sessions_router.get("/{game_session_id}")
async def get_game_session(game_session_id: str)->GameSessionMetadataApiModel:
    return service.get_game_session(game_session_id)


@game_sessions_router.delete("/{game_session_id}")
async def delete_game_session(game_session_id: str)->None:
    service.delete_game_session(game_session_id)


@game_sessions_router.post("/SaveState/{game_session_id}")
async def save_game_state(game_session_id: str, game_state: GameStateApiModel) -> GameStateApiModel:
    creation_request = GameStateApiModel(
        id=game_state.id,
        mainBoard=game_state.mainBoard,
        currentplayer=game_state.currentplayer
    )
    service.save_game_state(creation_request)
    return creation_request


@game_sessions_router.get("/GetState/{game_session_id}")
async def get_game_state_by_session(game_session_id: str):

    if game_session_id not in game_sessions_dict:
        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game session with ID {game_session_id} not found"
        )
    game_states = game_sessions_dict.get(game_session_id)
    if not game_states:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No game states found for session {game_session_id}"
        )
    return game_states



