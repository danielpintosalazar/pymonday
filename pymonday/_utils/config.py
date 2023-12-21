from dataclasses import dataclass, field
from pymonday._utils import validators


@dataclass
class MondayConfig:
    api_key: str = field(repr=False)
    api_url: str = field(init=False, repr=False,
                         default='https://api.monday.com/v2')
    api_file: str = field(init=False, repr=False,
                          default='https://api.monday.com/v2/file')

    def validate(self):
        for key in ['api_key', 'api_url', 'api_file']:
            if getattr(self, key) is None or getattr(self, key) == "":
                err = PyMondayError(f"Config value '{key}' must not be empty.")
                log.error(err, exc_info=True)
                raise err

    def __post_init__(self):
        self.validate()


@dataclass
class Config:
    monday: MondayConfig


def read_config():
    api_key = validators.exist_api_key()
    monday = MondayConfig(api_key)
    config = Config(monday=monday)
    return config
