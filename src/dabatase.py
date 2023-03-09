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

    for e in json_data:
        player = Player(**e)
        print(vars(player))


def save_players(players: List[Player]) -> None:
    """
    Sauvegarde tous les joueurs dans le fichier json "players.json
    :param players: liste des joueurs à sauvegarder
    :return: Rien
    """
    saved_players = get_players()
