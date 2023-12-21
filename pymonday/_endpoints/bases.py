from pydantic import BaseModel

class Model(BaseModel):
    """Base configuration for data model classes."""

    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True


class Service:
    """Base for services interacting with the Monday API over HTTP."""

    __slots__ = ("__weakref__",)
    pass