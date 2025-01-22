from typing import Dict
from fastapi import HTTPException, status
from src.ultimate_tic_tac_toe.DL.DB import Dictionary

class Services:
    def __init__(self):
        pass

    def create_game_session_dl(self, creation_request: dict) -> None:
        Dictionary[creation_request.id] = creation_request

    def list_game_sessions(self) -> dict:
        return Dictionary.values()

    def get_game_session(self, x: str) -> dict:
        game_session = Dictionary.get(game_session_id)
        if not game_session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Game session with ID {game_session_id} not found"
            )
        return game_session

    def delete_game_session(self, game_session_id: str) -> dict:
        game_session = Dictionary.pop(game_session_id, None)
        if not game_session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Game session with ID {game_session_id} not found"
            )
        return {"message": f"Game session with ID {game_session_id} has been deleted."}

    def save_game_state(self, game_session_id: str, creation_request: dict) -> None:
        Dictionary[game_session_id] = creation_request
