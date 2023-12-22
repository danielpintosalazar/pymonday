from dataclasses import dataclass, field
from pymonday._utils import config
from pymonday._utils.session import Session
from pymonday._endpoints.accounts import AccountService


@dataclass
class Client:

    def __init__(self):
        self.config: config.Config = config.read_config()
        self.session: Session = Session(
            api_key=self.config.monday.api_key,
            api_url=self.config.monday.api_url
        )
        self.accounts: AccountService = AccountService(session=self.session)
