from datetime import datetime as dt
from abc import ABC

class Action(ABC):
    """Abstract Action base class"""
    def __init__(self):
        """Initializes action"""
        # set timestamp
        self.ts = dt.now()