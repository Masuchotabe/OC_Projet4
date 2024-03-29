import os
import json
from models.players import Player
from models.tournaments import Tournament


class PlayerManager:
    """ Permet de gérer la sauvegarde et la liste de tous les joueurs"""

    def __init__(self, file_path: str = 'data/players.json'):
        self.file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_path)
        self._players = []
        self.load_players()

    def load_players(self):
        """
            Récupère tous les joueurs depuis le fichier json "players.json"
            :return: list[Player]
        """
        players = []

        if os.path.exists(self.file_path):
            with open(str(self.file_path), 'r') as file:
                json_data = json.load(file)

            for e in json_data:
                players.append(Player.from_dict(e))
        else:
            parent_dir_path = os.path.dirname(self.file_path)
            if not os.path.exists(parent_dir_path):
                os.makedirs(parent_dir_path)
        self._players = players

    def save_players(self):
        """
        Sauvegarde tous les joueurs dans le fichier json
        :return:
        """
        json_data = []
        for player in self._players:
            json_data.append(player.to_dict())

        with open(str(self.file_path), 'w+') as file:
            json.dump(json_data, file, indent=2)

    @property
    def players(self):
        """
        Property qui retourne une liste de joueur
        :return: [Player]
        """
        return self._players

    def get_player(self, national_chess_identifier):
        """
        Permet de récupérer un joueur par son identifiant national d'échec
        :param national_chess_identifier: Identifiant national d'échec
        :return: obj: Player
        """
        for player in self._players:
            if player.national_chess_identifier == national_chess_identifier:
                return player

    def add_player(self, player):
        """
        Ajoute un joueur
        :param player: objet player
        """
        self._players.append(player)
        self.save_players()

    def create_player(self, player_information):
        player = Player(**player_information)
        self.add_player(player)


class TournamentManager:
    """ Permet de gérer la sauvegarde et la liste de tous les tournois"""

    def __init__(self, file_path: str = 'data/tournaments.json'):
        self.file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_path)
        self._tournaments = []
        self.load_tournaments()

    def load_tournaments(self):
        """
            Récupère tous les tournois depuis le fichier json
            :return: list[Tournament]
        """
        tournaments = []

        if os.path.exists(self.file_path):
            with open(str(self.file_path), 'r') as file:
                json_data = json.load(file)

            for e in json_data:
                tournaments.append(Tournament.from_dict(e, player_manager=PlayerManager()))
        else:
            parent_dir_path = os.path.dirname(self.file_path)
            if not os.path.exists(parent_dir_path):
                os.makedirs(parent_dir_path)

        self._tournaments = tournaments

    def save_tournaments(self):
        """
        Sauvegarde tous les tournois dans le fichier json
        :return:
        """
        json_data = []
        for tournament in self._tournaments:
            json_data.append(tournament.to_dict())

        with open(str(self.file_path), 'w+') as file:
            json.dump(json_data, file, indent=2)

    @property
    def tournaments(self):
        """
        Property qui retourne une liste de tournois
        :return: [Tournament]
        """
        return self._tournaments

    def get_tournament(self, tournament_id: int) -> Tournament:
        """
        Permet de récupérer un tounrois par son identifiant
        :param tournament_id: Identifiant du tournois
        :return: obj: Tournament
        """
        pass

    def add_tournament(self, player) -> None:
        """
        Ajoute un joueur
        :param player:
        """
        self._tournaments.append(player)
        self.save_tournaments()

    def create_tournament(self, tournament_information):
        """
        Crée un tournoi avec les informations et un nouvel ID
        :param tournament_information : informations du tournoi
        """
        tournament = Tournament(identifier=self._get_new_identifier(), **tournament_information)
        self.add_tournament(tournament)

    def _get_new_identifier(self):
        """
        Génère un nouvel ID non existant pour le tournoi à partir de du nombre de tournois
        Sinon, cela prend le max des ID existant et ajoute 1
        :return: ID non existant dans la base
        """
        new_id = len(self._tournaments)+1
        id_list = [tournament.identifier for tournament in self._tournaments]
        if new_id in id_list:
            new_id = max(id_list)+1

        return new_id
