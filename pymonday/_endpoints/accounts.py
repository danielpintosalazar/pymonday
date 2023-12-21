import requests
from pymonday._endpoints import bases
from pymonday._utils.session import Session

from dataclasses import dataclass, field

@dataclass
class AccountService:
    session: Session

    def me():
        query = \
            """
            query {
                me {
                    id
                    name
                    created_at
                }
            }
            """

    pass