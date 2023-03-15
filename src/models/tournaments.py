from datetime import datetime
from typing import List

from src.models import Round
from src.dabatase import get_players


class Tournament:
    def __init__(self, name, location, start_date, players, end_date=None,
                 number_of_rounds=4, description=None, actual_round=1, players_scores=None, rounds=None):
        self.name = name
        self.description = description
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

        self.number_of_rounds = number_of_rounds
        self.actual_round = actual_round
        self.rounds = rounds

        self.players = players
        self.players_scores = ([{player.national_chess_identifier: 0} for player in players]
                               if not players_scores else players_scores)

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,

            'number_of_rounds': self.number_of_rounds,
            'actual_round': self.actual_round,
            'rounds': [round.to_dict() for round in self.rounds],

            'players': [player.national_chess_identifier for player in self.players],
            'players_scores': self.players_scores,
        }

    @classmethod
    def from_dict(cls, obj_dict):
        return cls(
            name=obj_dict['name'],
            description=obj_dict['description'],
            location=obj_dict['location'],
            start_date=obj_dict['start_date'],
            end_date=obj_dict['end_date'],
            number_of_rounds=obj_dict['number_of_rounds'],
            actual_round=obj_dict['actual_round'],
            rounds=[Round.from_dict(json_string) for json_string in obj_dict['rounds']],
            players=[player for player in get_players() if player.national_chess_identifier in obj_dict['players']],
            players_scores=obj_dict['players_scores'],
        )
