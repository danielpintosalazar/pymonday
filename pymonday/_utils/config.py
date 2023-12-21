import os
import logging
from dataclasses import dataclass, field
from dotenv import load_dotenv
from pymonday.errors import PyMondayError

log = logging.getLogger(__name__)
load_dotenv()


@dataclass
class MondayConfig:
    api_key: str = field(repr=False)
    api_url: str = field(init=False, repr=False)
    api_file: str = field(init=False, repr=False)

    def validate(self):
        for key in ['api_key']:
            if getattr(self, key) is None or getattr(self, key) == "":
                err = PyMondayError(f"Config value '{key}' must not be empty.")
                log.error(err, exc_info=True)
                raise err
            else:
                api_url = 'https://api.monday.com/v2'
                api_file = '%s/file' % api_url

    def __post_init__(self):
        self.validate()


@dataclass
class Config:
    monday: MondayConfig


def read_config():
    api_key = os.environ.get("PYMONDAY_API_KEY")
    if api_key is None or api_key == "":
        err = PyMondayError(
            "Environ value 'PYMONDAY_API_KEY' must be configurated.")
        log.error(err, exc_info=True)
        raise err
    else:
        monday = MondayConfig(api_key)
        config = Config(monday=monday)
        return config
