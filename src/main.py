from controllers import MainController


def main():
    my_app = MainController()
    my_app.run()


if __name__ == "__main__":
    main()

    pprint.pprint(tournament.to_dict())
    # with open('data/players.json', 'w') as file:
        # json.dump([vars(player_1), vars(player_2)], file, indent=2)

    # with open('data/players.json', 'r') as file:
    #     json_load = json.load(file)
    # get_players()

    # pprint.pprint(json_load)
    # my_tournament_reloaded = Tournament.from_dict(json_load)
