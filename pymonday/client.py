from dataclasses import dataclass, field
from pymonday._utils import config


@dataclass
class Client:
    config_path: str = None

    def __post_init__(self):
        self.config: config.Config = config.read_config()
