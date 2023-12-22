import requests
from pymonday._endpoints import bases
from pymonday._utils.session import Session

class AccountService(bases.Service):

    __slots__ = ("session")

    def __init__(self, session: Session):
        self.session: Session = session

    def me(self):
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
        
        response = self.session.get("https://google.com")
        return response