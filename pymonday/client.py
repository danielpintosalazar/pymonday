from dataclasses import dataclass, field
from pymonday._utils import config
from pymonday._utils import session


@dataclass
class Client:

    def __init__(self):
        self.config: config.Config = config.read_config()
        self.session: session.Config = session.read_session()
