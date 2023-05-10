import os.path
from typing import List
import json
from models import Player


# def get_players() -> List[Player]:
#     """
#     Récupère tous les joueurs depuis le fichier json "players.json"
#     :return: list[Player]
#     """
#     with open('data/players.json', 'r')as file:
#         json_data = json.load(file)
#
#     players = []
#     for e in json_data:
#         players.append(Player(**e))
#
#     return players
#
# # TODO : créer un truc du style PlayerManager ?
#
#
# def get_player(national_chess_identifier: str) -> Player:
#     """
#
#     :param national_chess_identifier: Identifiant national d'échec
#     :return: le joueur avec cet identifiant
#     """
#     players = get_players()
#     for player in players:
#         if player.national_chess_identifier == national_chess_identifier:
#             return player
#     else:
#         return None
#
#
# def save_players(players: List[Player]) -> None:
#     """
#     Sauvegarde tous les joueurs dans le fichier json "players.json
#     :param players: liste des joueurs à sauvegarder
#     :return: Rien
#     """
#     saved_players = get_players()


class PlayerManager:
    """ Permet de gérer la sauvegarde et la liste de tous les joueurs"""

    def __init__(self, file_path: str = 'data/players.json'):
        self.file_path = file_path
        self._players = []
        self.load_players()

    def load_players(self):
        """
            Récupère tous les joueurs depuis le fichier json "players.json"
            :return: list[Player]
        """
        with open(str(self.file_path), 'r') as file:
            json_data = json.load(file)

        players = []
        for e in json_data:
            players.append(Player(**e))
        self._players = players

    def save_players(self):
        """
        Sauvegarde tous les joueurs dans le fichier json
        :return:
        """
        json_data = []
        for player in self._players:
            json_data.append(player.to_dict())

        with open(str(self.file_path), 'w') as file:
            json.dump(json_data, file, indent=2)

    @property
    def players(self):
        """
        Property qui retourne une liste de joueur
        :return: [Player]
        """
        return self._players

    def get_player(self, national_chess_identifier: str) -> Player:
        """
        Permet de récupérer un joueur par son identifiant national d'échec
        :param national_chess_identifier: Identifiant national d'échec
        :return: obj: Player
        """
        for player in self._players:
            if player.national_chess_identifier == national_chess_identifier:
                return player

    def add_player(self, player) -> None:
        """
        Ajoute un joueur
        :param player:
        """
        self._players.append(player)
        self.save_players()

    def create_player(self, player_information):
        player = Player(**player_information)
        self.add_player(player)


