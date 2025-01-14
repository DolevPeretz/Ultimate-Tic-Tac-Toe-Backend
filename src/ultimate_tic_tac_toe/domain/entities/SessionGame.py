import uuid
from datetime import datetime
from src.ultimate_tic_tac_toe.domain.entities.MainBoard import MainBoard
from src.ultimate_tic_tac_toe.domain.enums.game_difficulty_level import GameDifficultyLevel
from src.ultimate_tic_tac_toe.domain.enums.state_game import StateGame
from pydantic.alias_generators import to_camel


class GameSession:
    def __init__(self, difficultyLevel: GameDifficultyLevel = GameDifficultyLevel.easy):
        self.difficultyLevel = difficultyLevel
        self.id = None
        self.name = None
        self.title = None
        self.status = StateGame.in_progress
        self.create_time = datetime.now()
        self.update_time = None
        self.main_board = MainBoard()

    def start_game(self):
        self.id=str(uuid.uuid4())
        self.status = StateGame.in_progress
        self.update_time = datetime.now()
        self.create_time = datetime.now()
        self.name = str(uuid.uuid4())
        self.title = ""
        game_state = self.__dict__



        return  game_state

    @staticmethod
    def get_game_by_id(game_sessions_db, game_session_id: str):
        return next((game for game in game_sessions_db if game["id"] == game_session_id), None)

    @staticmethod
    def delete_game_by_id(game_sessions_db, game_session_id):
        for game_session in game_sessions_db:
            if game_session.id == game_session_id:
                game_sessions_db.remove(game_session)
                return {"message": f"Game session {game_session_id} deleted successfully."}
        return {"message": "Game session not found."}
