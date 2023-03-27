from typing import List
import json
from models import Player


def get_players() -> List[Player]:
    """
    Récupère tous les joueurs depuis le fichier json "players.json"
    :return: list[Player]
    """
    with open('data/players.json', 'r')as file:
        json_data = json.load(file)

    players = []
    for e in json_data:
        players.append(Player(**e))

    return players

# TODO : créer un truc du style PlayerManager ?


def get_player(national_chess_identifier: str) -> Player:
    """

    :param national_chess_identifier: Identifiant national d'échec
    :return: le joueur avec cet identifiant
    """
    players = get_players()
    for player in players:
        if player.national_chess_identifier == national_chess_identifier:
            return player
    else:
        return None


def save_players(players: List[Player]) -> None:
    """
    Sauvegarde tous les joueurs dans le fichier json "players.json
    :param players: liste des joueurs à sauvegarder
    :return: Rien
    """
    saved_players = get_players()
