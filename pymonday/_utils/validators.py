import os
import logging
from dotenv import load_dotenv
from pymonday.errors import PyMondayError

log = logging.getLogger(__name__)
load_dotenv()

def exist_api_key():
    api_key = os.environ.get("PYMONDAY_API_KEY")
    if api_key is None or api_key == "":
        err = PyMondayError(
            "Environ value 'PYMONDAY_API_KEY' must be configurated.")
        log.error(err, exc_info=True)
        raise err
    else:
        return api_key