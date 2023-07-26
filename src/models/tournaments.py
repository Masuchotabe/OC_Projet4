import random
from datetime import datetime
from typing import List

from src.models import Round, Player, Match


class Tournament:
    def __init__(self, identifier, name, location, start_date, players: List[Player]=None, end_date=None,
                 number_of_rounds=4, description=None, actual_round_number=0, players_scores=None, rounds=None):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

        self.number_of_rounds = int(number_of_rounds)
        self.actual_round_number = actual_round_number
        self.rounds = rounds or []

        self.players = players or []
        self.players_scores = ({player.national_chess_identifier: 0 for player in players}
                               if not players_scores and players else players_scores)

    def __repr__(self):
        return f"{self.name} - {self.location} - {self.start_date}"

    def to_dict(self):
        return {
            'identifier': self.identifier,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,

            'number_of_rounds': self.number_of_rounds,
            'actual_round_number': self.actual_round_number,
            'rounds': [round.to_dict() for round in self.rounds],

            'players': [player.national_chess_identifier for player in self.players],
            'players_scores': self.players_scores,
        }

    @classmethod
    def from_dict(cls, obj_dict, player_manager):
        return cls(
            identifier=obj_dict['identifier'],
            name=obj_dict['name'],
            description=obj_dict['description'],
            location=obj_dict['location'],
            start_date=obj_dict['start_date'],
            end_date=obj_dict['end_date'],
            number_of_rounds=obj_dict['number_of_rounds'],
            actual_round_number=obj_dict['actual_round_number'],
            rounds=[Round.from_dict(round_dict, player_manager) for round_dict in obj_dict['rounds']],
            players=[
                player for player in player_manager.players if player.national_chess_identifier in obj_dict['players']
            ],
            players_scores=obj_dict['players_scores'],
        )

    @property
    def matches(self):
        """
        Propriété permettant de récuperer tous les matchs du tournoi
        :return: all_matches [List]
        """
        all_matches = []
        for round in self.rounds:
            if round.matches:
                all_matches.extend(round.matches)
        return all_matches

    def is_started(self):
        """
        Permet de savoir si un tournoi est commencé.
        :return: True ou False
        """
        if len(self.players) > 0 and len(self.rounds) > 0 and self.actual_round_number != 0:
            return True
        else:
            return False

    def is_finished(self):
        """
        Permet de savoir si un tournoi est terminé en vérifiant
        que tous les rounds ont une date de fin et que le
        round actuel est le dernier.
        :return: True ou False
        """
        if all([r.is_finished() for r in self.rounds]) and (self.actual_round_number == self.number_of_rounds):
            return True
        else:
            return False

    def get_actual_round(self):
        """
        Permet de récupérer le round actuel.
        :return:
        """
        for r in self.rounds:
            if r.round_number == self.actual_round_number:
                return r
        return None

    def get_ordered_player_list(self):
        ordered_player_rank = sorted(self.players_scores.items(), key=lambda item: (-item[1], item[0]))
        ordered_player_list = []
        for player_id, score in ordered_player_rank:
            for player in self.players:
                if player.national_chess_identifier == player_id:
                    ordered_player_list.append(player)
        return ordered_player_list

    def init_players_score(self):
        self.players_scores = {player.national_chess_identifier: 0.0 for player in self.players}

    def update_players_score(self):
        """
        Met à jour le score des joueurs global du tournoi
        """
        self.init_players_score()
        for match in self.matches:
            if (match.score_1 is not None) and (match.score_2 is not None):
                self.players_scores[match.player_1.national_chess_identifier] += match.score_1
                self.players_scores[match.player_2.national_chess_identifier] += match.score_2


    """
    TODO : 
        - démarrer un nouveau round : 
            - Methode get_match if rounds 
            - si pas pas de rounds, randomize la liste des joueurs 
            - si rounds, alors on liste les joueurs par classement 
                - on génère les paires 
    """
