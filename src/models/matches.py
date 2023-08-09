from models.players import Player


class Match:
    def __init__(self, player_1: Player, player_2: Player, score_1=None, score_2=None):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def __repr__(self):
        if (self.score_1 is not None) and (self.score_2 is not None):
            return f"{self.player_1} - {self.score_1} | {self.player_2} - {self.score_2}"
        else:
            return f"{self.player_1} | {self.player_2}"

    def __eq__(self, other):
        if isinstance(other, Match):
            other_player_id = [other.player_1.national_chess_identifier, other.player_2.national_chess_identifier]
            my_player_id = [self.player_1.national_chess_identifier, self.player_2.national_chess_identifier]
            return sorted(other_player_id) == sorted(my_player_id)

        return False

    def to_dict(self):
        """
        Génère un dictionnaire à partir de l'objet
        :return: dict de l'objet match
        """
        return {
            "player_1": self.player_1.national_chess_identifier,
            "player_2": self.player_2.national_chess_identifier,
            "score_1": self.score_1,
            "score_2": self.score_2,
        }

    @classmethod
    def from_dict(cls, obj_dict, player_manager):
        """
        Crée un objet Match à partir d'un dictionnaire
        :param obj_dict: dictionnaire avec les données du Match
        :param player_manager: Obj permettant de gérer les joueurs
        :return: Objet Match
        """
        return cls(
            player_1=player_manager.get_player(national_chess_identifier=obj_dict['player_1']),
            player_2=player_manager.get_player(national_chess_identifier=obj_dict['player_2']),
            score_1=obj_dict['score_1'],
            score_2=obj_dict['score_2'],
        )

    def has_result(self):
        """
        Permet de savoir si le match à un résultat de renseigné
        :return: True si le score est renseigné sinon False
        """
        return self.score_1 is not None and self.score_2 is not None
