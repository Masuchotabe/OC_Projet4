from datetime import datetime
from typing import List
from src.models import Player
from src.dabatase import get_player


class Match:
    def __init__(self, player_1: Player, player_2: Player, score_1=None, score_2=None):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def __repr__(self):
        return (
            [self.player_1, self.score_1],
            [self.player_2, self.score_2]
        )

    def to_dict(self):
        return {
            "player_1": self.player_1.national_chess_identifier,
            "player_2": self.player_2.national_chess_identifier,
            "score_1": self.score_1,
            "score_2": self.score_2,
        }

    @classmethod
    def from_dict(cls, obj_dict):
        return cls(
            player_1=get_player(national_chess_identifier=obj_dict['player_1']),
            player_2=get_player(national_chess_identifier=obj_dict['player_2']),
            score_1=obj_dict['score_1'],
            score_2=obj_dict['score_2'],
        )
