from src.ultimate_tic_tac_toe.api.models.api_model_base import ApiModelBase
from src.ultimate_tic_tac_toe.domain.enums.game_difficulty_level import GameDifficultyLevel
from pydantic.fields import Field

class GameSessionCreationRequestApiModel(ApiModelBase):
    difficultyLevel: GameDifficultyLevel = Field(..., description="The game session starting difficulty level, can be modified mid-game")
