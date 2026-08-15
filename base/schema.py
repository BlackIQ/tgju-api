# Libs
from pydantic import BaseModel, ConfigDict  # Pydantic


# Base Class: Schema
class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
