from fastapi import HTTPException, status
from src.ultimate_tic_tac_toe.DL.DB import Dictionary


class Services:
    def __init__(self):
        pass

    def create_game_session_dl(self,creation_request) -> None:
        Dictionary[creation_request.id] = creation_request

    def list_game_sessions(self) -> Dictionary:
        return Dictionary.values()

    def get_game_session(self,game_session_id: str):
        game_session = Dictionary.get(game_session_id)
        if not game_session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Game session with ID {game_session_id} not found"
            )
        return game_session



    def delete_game_session(self,game_session_id: str):
        game_session = Dictionary.pop(game_session_id, None)
        if not game_session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Game session with ID {game_session_id} not found"
            )
        return {"message": f"Game session with ID {game_session_id} has been deleted."}

    def save_game_state(game_session_id: str, creation_request) :

        Dictionary[id] = creation_request

    # def get_game_state_by_session(game_session_id: str):
















