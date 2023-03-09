from models import Player, Tournament, Round, Match
import json
import pprint

from dabatase import get_players

if __name__ == "__main__":

    player_1 = Player("toto", "nom", "05/02/1997", "BA25455")
    player_2 = Player("toto2", "nom", "05/08/1997", "GF49489")
    print(player_1)
    players = [player_1, player_2]
    tournament = Tournament('first_one', players, 'tours', 'today', 'date de fin')

    pprint.pprint(vars(tournament))
    with open('data/players.json', 'w') as file:
        json.dump([vars(player_1), vars(player_2)], file, indent=2)

    # with open('data/players.json', 'r') as file:
    #     json_load = json.load(file)
    get_players()

    # pprint.pprint(json_load)
    # my_tournament_reloaded = Tournament.from_dict(json_load)
