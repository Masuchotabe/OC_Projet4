from models import Player, Tournament, Round, Match
import json
import pprint

from dabatase import get_players

if __name__ == "__main__":

    player_1 = Player("toto", "nom", "05/02/1997", "BA25455")
    player_2 = Player("toto2", "nom", "05/08/1997", "GF49489")
    player_3 = Player("toto3", "nom", "05/12/1997", "HJ75847")
    player_4 = Player("toto4", "nom", "05/05/1997", "PO35821")

    players = [player_1, player_2, player_3, player_4]

    match_1 = Match(player_1, player_2)
    match_2 = Match(player_3, player_4)

    round_1 = Round("rpund 1", [match_1, match_2])
    tournament = Tournament('first_one', 'tours', 'today', players, 'end_date', rounds=[round_1, ])

    pprint.pprint(tournament.to_dict())
    # with open('data/players.json', 'w') as file:
        # json.dump([vars(player_1), vars(player_2)], file, indent=2)

    # with open('data/players.json', 'r') as file:
    #     json_load = json.load(file)
    # get_players()

    # pprint.pprint(json_load)
    # my_tournament_reloaded = Tournament.from_dict(json_load)
