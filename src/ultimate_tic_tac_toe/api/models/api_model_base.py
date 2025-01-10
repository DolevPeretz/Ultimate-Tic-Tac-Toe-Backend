from pydantic import BaseModel, ConfigDict
from pydantic.fields import FieldInfo, ComputedFieldInfo
from pydantic.alias_generators import to_camel

def _snake_to_title(snake_str: str) -> str:
    return ' '.join(word.capitalize() for word in snake_str.split('_'))

def _field_title_generator(field_name: str, field_info: FieldInfo | ComputedFieldInfo) -> str:
    return _snake_to_title(field_name)

class ApiModelBase(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, field_title_generator=_field_title_generator, populate_by_name=True)