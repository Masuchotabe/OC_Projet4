import random
from datetime import datetime
from typing import List

from src.models import Round, Player, Match
from src.dabatase import get_players


class Tournament:
    def __init__(self, name, location, start_date, players: List[Player]=None, end_date=None,
                 number_of_rounds=4, description=None, actual_round=0, players_scores=None, rounds=None):
        self.name = name
        self.description = description
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

        self.number_of_rounds = number_of_rounds
        self.actual_round = actual_round
        self.rounds = rounds or []

        self.players = players or []
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
            rounds=[Round.from_dict(round_dict) for round_dict in obj_dict['rounds']],
            players=[player for player in get_players() if player.national_chess_identifier in obj_dict['players']],
            players_scores=obj_dict['players_scores'],
        )

    def start_round(self):
        """
        Fonction permettant de commencer un nouveau round. Les matchs sont créées selon des conditions:
        :return:
        """
        if len(self.rounds) > 0:  # On classe
            pass
        else:  # on mélange les joueurs
            players_list = self.players
            random.shuffle(players_list)
            new_matches = [Match(player_1=x, player_2=y) for x, y in zip(players_list[::2], players_list[1::2])]


        self.rounds.append(Round(f"Round {self.actual_round+1}", new_matches))




    @property
    def matches(self):
        """
        Propriété permettant de récuperer tous les matchs du tournois
        :return: all_matches [List]
        """
        all_matches = []
        for round in self.rounds:
            if round.matches:
                all_matches.append(round.matches)
        return all_matches

    """
    TODO : 
        - démarrer un nouveau round : 
            - Methode get_match if rounds 
            - si pas pas de rounds, randomize la liste des joueurs 
            - si rounds, alors on liste les joueurs par classement 
                - on génère les paires 
    """
