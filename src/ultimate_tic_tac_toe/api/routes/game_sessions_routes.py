from datetime import datetime
from fastapi import APIRouter
from src.ultimate_tic_tac_toe.api.models.game_state_api_model import GameStateApiModel
from src.ultimate_tic_tac_toe.api.models.game_session_creation_request_api_model import GameSessionCreationRequestApiModel
from src.ultimate_tic_tac_toe.api.models.game_session_metadata_api_model import GameSessionMetadataApiModel
from src.ultimate_tic_tac_toe.domain.enums.game_status import GameStatus
from src.ultimate_tic_tac_toe.BL.services import Services


game_sessions_router = APIRouter(prefix="/gameSessions")
game_sessions_dict={}
service=Services()

@game_sessions_router.post("")
async def create_game_session(creation_request: GameSessionCreationRequestApiModel) -> GameSessionMetadataApiModel:
    game_session_title = ""
    game_session_status = GameStatus.in_progress
    game_session_difficulty = creation_request.difficultyLevel
    current_time = datetime.now()
    state = "" 

    game_session = GameSessionMetadataApiModel(
        title=game_session_title,
        status=game_session_status,
        difficulty_level=game_session_difficulty,
        create_time=current_time,
        update_time=current_time,
        state=state  
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
        mainBoard=game_state.mainBoard,
        currentplayer=game_state.currentplayer
    )
    service.save_game_state(game_session_id,creation_request)
    return creation_request


@game_sessions_router.get("/GetState/{game_session_id}")
async def get_game_state_by_session(game_session_id: str):
    game_states= service.load_game_state(game_session_id)
    return game_states

    




