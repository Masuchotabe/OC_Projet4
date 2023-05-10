from datetime import datetime
from typing import List

from .matches import Match


class Round:
    def __init__(self, name, matches: List[Match], start_date: datetime = None, end_date: datetime = None):
        self.name = name
        self.start_date = start_date if start_date else datetime.now()
        self.end_date = end_date
        self.matches = matches

    def to_dict(self):
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": [match.to_dict() for match in self.matches],
        }

    @classmethod
    def from_dict(cls, obj_dict, player_manager):
        return cls(
            name=obj_dict['name'],
            start_date=obj_dict['start_date'],
            end_date=obj_dict['end_date'],
            matches=[Match.from_dict(match_dict, player_manager) for match_dict in obj_dict['matches']],
        )
