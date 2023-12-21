from dataclasses import dataclass, field
from requests import Session as RequestSession
from pymonday._utils import validators


@dataclass
class MondaySession:
    api_key: str = field(repr=False)
    current: RequestSession = field(init=False, repr=False)

    def default_session(self):
        self.current = RequestSession()
        self.current.headers['Authorization'] = self.api_key

    def __post_init__(self):
        self.default_session()


@dataclass
class Config:
    monday: MondaySession


def read_session():
    api_key = validators.exist_api_key()
    monday = MondaySession(api_key)
    config = Config(monday=monday)
    return config
