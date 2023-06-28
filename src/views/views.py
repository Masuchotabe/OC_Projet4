
class MainView:
    """
    Classe définissant la vue de base
    """
    def __init__(self):
        print("""
        #############################################
        ###### Gestion de tournois d'échecs #########
        #############################################
        """)

    def show_menu(self, choices):
        """
        Affiche un menu à l'utilisateur et retourne le choix
        :param choices:
        :return:
        """
        valid_result = False
        while not valid_result:

            for index, choice in enumerate(choices, start=1):
                print(f"{index} - {choice}")
            user_input = input("Veuillez choisir un menu : ")
            if user_input.isnumeric():
                if 0 < int(user_input) <= len(choices):
                    return int(user_input)

            print(f"ERREUR : Veuillez renseigner un entier compris entre 1 et {len(choices)}")

    def prompt_for_new_player(self):
        print("Veuillez renseigner les informations du nouveau joueur : ")
        first_name = input("Son prénom : \n")
        last_name = input("Son nom de famille : \n")
        birth_date = input("Sa date de naissance : \n")
        national_chess_identifier = input("Son identifiant national d'échecs : \n")
        return {'first_name': first_name,
                'last_name': last_name,
                'birth_date': birth_date,
                'national_chess_identifier': national_chess_identifier}

    def prompt_for_new_tournament(self):
        print("Veuillez renseigner les informations du nouveau tournois : ")
        name = input("Son nom : \n")
        description = input("Sa description : \n")
        location = input("Son lieu : \n")
        number_of_rounds = input("nombre de tours : \n")
        start_date = input("Sa date de début : \n")
        end_date = input("Sa date de fin : \n")

        return {'name': name,
                'description': description,
                'location': location,
                'number_of_rounds': number_of_rounds,
                'start_date': start_date,
                'end_date': end_date
                }

    def show_players_list(self, players):
        for player in players:
            print(f"{player} - {player.national_chess_identifier}")

    def show_tournaments_list(self, tournaments):
        for tournament in tournaments:
            print(tournament)

    def prompt_for_player_id(self, player_list):
        """
        Retourne l'id ( national chess identifier) d'un joueur parmis la liste.



        Par défaut, l'id du premier joueur de la liste.
        :param player_list: liste des joueurs sélectionnable
        :return: un ID de joueur
        """
        print("Liste des joueurs : ")
        self.show_players_list(player_list)
        first_player_id = player_list[0].national_chess_identifier
        player_id = input(f"Renseigner l'identifiant national d’échecs du joueur :[{first_player_id}]")
        if player_id:
            return player_id
        else:
            return first_player_id
