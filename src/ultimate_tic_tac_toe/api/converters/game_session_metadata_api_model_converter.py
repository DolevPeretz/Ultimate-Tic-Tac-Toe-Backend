from src.ultimate_tic_tac_toe.api.models.game_session_metadata_api_model import GameSessionMetadataApiModel
class GameSessionMetadata:
    pass

class GameSessionMetadataApiModelConverter:

    @staticmethod
    def to_api_model(session_metadata: GameSessionMetadata) -> GameSessionMetadataApiModel:
        return GameSessionMetadataApiModel(  
            game_id=session_metadata.game_id,
            game_name=session_metadata.game_name,
            title=session_metadata.title,
            status=session_metadata.status,
            difficulty_level=session_metadata.difficulty_level,
            create_time=session_metadata.create_time,
            update_time=session_metadata.update_time,
            state=session_metadata.state,
        )

    @staticmethod
    def from_api_model(api_model: GameSessionMetadataApiModel) -> GameSessionMetadata:
        return GameSessionMetadata(
            game_id=api_model.game_id,
            game_name=api_model.game_name,
            title=api_model.title,
            status=api_model.status,
            difficulty_level=api_model.difficulty_level,
            create_time=api_model.create_time,
            update_time=api_model.update_time,
            state=api_model.state,

        )
