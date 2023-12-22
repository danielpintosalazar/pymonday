from dataclasses import dataclass, field
from requests import Session as RequestSession
from pymonday._utils import validators


class Session(RequestSession):
    def __init__(
        self,
        api_key: str,
        api_url: str
    ) -> None:
        super().__init__()
        self.headers['Authorization'] = api_key