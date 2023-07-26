from datetime import datetime
from typing import List

from .matches import Match


class Round:
    def __init__(self, name, round_number, matches: List[Match], start_date: datetime = None, end_date: datetime = None):
        self.name = name
        self.round_number = round_number
        self.start_date = start_date if start_date else datetime.now()
        self.end_date = end_date
        self.matches = matches

    def __repr__(self):
        return f"{self.name}"

    def to_dict(self):
        return {
            "name": self.name,
            "round_number": self.round_number,
            "start_date": self.start_date.strftime('%Y-%m-%d %H:%M:%S'),
            "end_date": self.end_date.strftime('%Y-%m-%d %H:%M:%S') if self.end_date else None,
            "matches": [match.to_dict() for match in self.matches],
        }

    @classmethod
    def from_dict(cls, obj_dict, player_manager):
        return cls(
            name=obj_dict['name'],
            round_number=obj_dict['round_number'],
            start_date=datetime.strptime(obj_dict['start_date'], '%Y-%m-%d %H:%M:%S'),
            end_date=datetime.strptime(obj_dict['end_date'], '%Y-%m-%d %H:%M:%S') if obj_dict['end_date'] else None,
            matches=[Match.from_dict(match_dict, player_manager) for match_dict in obj_dict['matches']],
        )

    def is_finished(self):
        """
        Permet de savoir si le round est fini
        :return: True si end_date est renseigné, sinon false
        """
        return True if self.end_date and self.are_all_match_results_complete() else False

    def are_all_match_results_complete(self):
        """
        Permet de vérifier que tous les matchs ont bien un score de renseigné
        :return: True si tout les matchs ont un résultat
        """
        return all([match.has_result() for match in self.matches])

    def finish(self):
        """
        Cloture le Round
        """
        self.end_date = datetime.now()
