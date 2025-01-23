from typing import Dict, Any
from fastapi import HTTPException, status
from src.ultimate_tic_tac_toe.DL.DB import Dictionary,Dictionary_state

class Services:
    def __init__(self):
        pass

    def create_game_session_dl(self, creation_request: dict[str, Any]) -> None:
        Dictionary[creation_request['id']] = creation_request

    def list_game_sessions(self) -> dict[str, Any]:
        return Dictionary.values()

    def get_game_session(self, game_session_id: str) -> dict[str, Any]:
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

    def save_game_state(self, game_session_id: str, creation_request: dict[str, Any]) -> None:
        game_session = Dictionary.get(game_session_id)
        if not game_session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Game session with ID {game_session_id} not found"
            )
        Dictionary[game_session_id].state=creation_request.id
        Dictionary_state[creation_request.id] = creation_request
        
    def load_game_state(self, game_session_id: str)->dict[str, Any]:
        game_session = Dictionary.get(game_session_id)
        if not game_session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Game session with ID {game_session_id} not found"
            )
        sys_id_game_state=Dictionary[game_session_id].state
        return Dictionary_state.get(sys_id_game_state)
        
