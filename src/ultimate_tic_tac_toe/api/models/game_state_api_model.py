import uuid
from typing import List
from src.ultimate_tic_tac_toe.api.models.api_model_base import ApiModelBase
from pydantic.fields import Field
from src.ultimate_tic_tac_toe.domain.enums.current_player import Current_Player



class GameStateApiModel(ApiModelBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="The game session unique id")
    mainBoard: List[List[Current_Player | None ]]=   Field(..., description="List Of Option state")
    currentplayer:  Current_Player = Field(..., description="The Current Player X or O")



