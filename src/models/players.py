from datetime import datetime
from typing import List


class Player:
    def __init__(self, first_name: str, last_name: str, birth_date: datetime.date, national_chess_identifier: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.national_chess_identifier = national_chess_identifier

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        return self.national_chess_identifier == other.national_chess_identifier

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, obj_dict):
        return cls(**obj_dict)
