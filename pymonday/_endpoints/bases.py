from pydantic import BaseModel

class Model(BaseModel):
    """Base configuration for data model classes."""

    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True