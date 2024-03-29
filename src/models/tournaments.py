from datetime import datetime

from models.rounds import Round


class Tournament:
    def __init__(self, identifier, name, location, start_date, players=None, end_date=None,
                 number_of_rounds=4, description=None, actual_round_number=0, players_scores=None, rounds=None):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.location = location
        if isinstance(start_date, str):
            self.start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
        else:
            self.start_date = start_date

        if isinstance(end_date, str):
            self.end_date = datetime.strptime(end_date, '%d/%m/%Y').date()
        else:
            self.end_date = end_date

        self.number_of_rounds = int(number_of_rounds)
        self.actual_round_number = actual_round_number
        self.rounds = rounds or []

        self.players = players or []
        self.players_scores = ({player.national_chess_identifier: 0 for player in players}
                               if not players_scores and players else players_scores)

    def __repr__(self):
        if self.is_finished():
            return f"{self.name} - {self.location} - {self.start_date} - {self.end_date} - TERMINE"
        elif self.is_started():
            return f"{self.name} - {self.location} - {self.start_date} - {self.end_date} - EN COURS"
        return f"{self.name} - {self.location} - {self.start_date} - {self.end_date} - NON DEMARRE"

    def to_dict(self):
        """
        Génère un dictionnaire à partir de l'objet
        :return: dict de l'objet tournament
        """
        return {
            'identifier': self.identifier,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            "start_date": self.start_date.strftime('%Y-%m-%d') if self.start_date else None,
            "end_date": self.end_date.strftime('%Y-%m-%d') if self.end_date else None,

            'number_of_rounds': self.number_of_rounds,
            'actual_round_number': self.actual_round_number,
            'rounds': [round.to_dict() for round in self.rounds],

            'players': [player.national_chess_identifier for player in self.players],
            'players_scores': self.players_scores,
        }

    @classmethod
    def from_dict(cls, obj_dict, player_manager):
        """
        Crée un objet Tournament à partir d'un dictionnaire
        :param obj_dict: dictionnaire avec les données du Tournament
        :param player_manager: Obj permettant de gérer les joueurs
        :return: Objet Tournament
        """
        return cls(
            identifier=obj_dict['identifier'],
            name=obj_dict['name'],
            description=obj_dict['description'],
            location=obj_dict['location'],
            start_date=datetime.strptime(obj_dict['start_date'], '%Y-%m-%d').date(),
            end_date=(
                datetime.strptime(obj_dict['end_date'], '%Y-%m-%d').date() if obj_dict['end_date'] else None
            ),
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

    def can_start(self):
        """
        Permet de vérifier qu'un tournoi différents prérequis pour démarrer :
            - Nombre de joueurs pairs
            - Le nombre de tours est cohérent avec le nombre de joueurs
            pour qu'ils puissent jouer sans se rencontrer 2 fois.
        :return: True si le tournoi respectent les conditions.
        """
        player_len = len(self.players)
        if (player_len % 2 == 0) and player_len > 0:  # Nombre de joueurs pairs et >0
            number_of_rounds = self.number_of_rounds
            if number_of_rounds < player_len:  # on vérifie si le nombre de tours est inférieur au nombre de joueur.
                return True
        # Sinon on return false
        return False

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
        """
        Permet d'obtenir la liste des joueurs ordonnée par leur nombre de points et ordre alphabétique
        :return: List des players triés
        """
        ordered_player_rank = sorted(self.players_scores.items(), key=lambda item: (-item[1], item[0]))
        ordered_player_list = []
        for player_id, score in ordered_player_rank:
            for player in self.players:
                if player.national_chess_identifier == player_id:
                    ordered_player_list.append(player)
        return ordered_player_list

    def get_ranked_player_list(self):
        """
        Génère une liste de dictionnaire contenant pour chaque dictionnaire le joueur, son score et son rang.
        :return:
        """
        player_dict_list = []
        for index, player in enumerate(self.get_ordered_player_list(), start=1):
            player_dict = dict()
            player_dict['rank'] = index
            player_dict['score'] = self.players_scores[player.national_chess_identifier]
            player_dict.update(player.to_dict())
            player_dict_list.append(player_dict)
        return player_dict_list

    def init_players_score(self):
        """
        Initialise les scores des joueurs à 0
        """
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
