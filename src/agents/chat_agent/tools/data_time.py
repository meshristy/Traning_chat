import time
from langchain.tools import tool

@tool
def get_current_date_and_time() -> str:
    """
    Returns the current system date and time in human readable format.
    """
    return time.ctime()
