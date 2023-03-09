from datetime import datetime
from typing import List


class Tournament:
    def __init__(self, name, players, location, start_date, end_date,
                 number_of_rounds=4, description=None, actual_round=1):
        self.name = name
        self.players = players
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.actual_round = actual_round
        self.players_scores = [{player.national_chess_identifier: 0} for player in players]

    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'number_of_rounds': self.number_of_rounds,
            'description': self.description,
            'actual_round':self.actual_round,
            'players': [player.national_chess_identifier for player in self.players],
            'players_scores': self.players_scores,
        }

    def from_dict(self, obj_dict):
        pass
