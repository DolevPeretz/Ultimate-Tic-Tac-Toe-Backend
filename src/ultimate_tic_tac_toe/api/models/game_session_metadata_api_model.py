from datetime import datetime
from src.ultimate_tic_tac_toe.api.models.api_model_base import ApiModelBase
from pydantic.fields import Field
from src.ultimate_tic_tac_toe.domain.enums.game_difficulty_level import GameDifficultyLevel
from src.ultimate_tic_tac_toe.domain.enums.state_game import StateGame


class GameSessionMetadataApiModel(ApiModelBase):
    id: str = Field(..., description="The game session unique id")
    name: str = Field(..., description="The resource unique name which can be used as URI")
    title: str = Field(..., description="The game session title used for display purposes to distinguish between saved game sessions")
    # game_state_info - add this field when you have some representation for game state
    status:  StateGame = Field(..., description="The state of the Game- Complete/in Progress")
    difficulty_level: GameDifficultyLevel = Field(..., description="The game difficulty level, can be modified mid-game")
    create_time: datetime
    update_time: datetime
