from datetime import datetime
from typing import List

from .matches import Match


class Round:
    def __init__(self, name, matches: List[Match]):
        self.name = name
        self.start_date = datetime.now()
        self.matches = matches
