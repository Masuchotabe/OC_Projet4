import os

from tabulate import tabulate

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

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self, choices, message = None):
        self.clear_console()
        """
        Affiche un menu à l'utilisateur et retourne le choix
        :param choices:
        :return:
        """
        valid_result = False
        while not valid_result:

            for index, choice in enumerate(choices, start=1):
                print(f"{index} - {choice}")
            if message:
                user_input = input(message)
            else:
                user_input = input("Veuillez choisir un menu : ")
            if user_input.isnumeric():
                if 0 < int(user_input) <= len(choices):
                    return int(user_input)

            print(f"ERREUR : Veuillez renseigner un entier compris entre 1 et {len(choices)}")

    def prompt_for_new_player(self):
        self.clear_console()
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
        self.clear_console()
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
        self.clear_console()
        property_list = ["first_name", "last_name", "birth_date", "national_chess_identifier"]
        headers = ["Prénom", "Nom", "Date de naissance", "Identifiant national d'échecs"]
        self.print_list_of_object(players, property_list, headers)

    def show_tournaments_list(self, tournaments):
        self.clear_console()
        property_list = ["name", "location", "start_date", "end_date", "description"]
        headers = ["Nom", "Lieu", "Date de début", "Date de fin", "Description"]
        self.print_list_of_object(tournaments, property_list, headers)

    def show_tournament(self, tournament):
        self.clear_console()

        print(f"Tournois {tournament.name} du {tournament.start_date} au {tournament.end_date}")
        for round in tournament.rounds:
            if round.round_number != tournament.actual_round_number:
                print(f"{round.name}")
            else:
                print(f"{round.name} - Round actuel")

    def show_round(self, round):
        self.clear_console()
        print(round.name)
        for match in round.matches:
            print(match)

    def prompt_for_player_id(self, player_list):
        """
        Retourne l'id ( national chess identifier) d'un joueur parmis la liste.
        Par défaut, l'id du premier joueur de la liste.
        :param player_list: liste des joueurs sélectionnable
        :return: un ID de joueur
        """
        self.clear_console()

        print("Liste des joueurs : ")
        self.show_players_list(player_list)
        first_player_id = player_list[0].national_chess_identifier
        player_id = input(f"Renseigner l'identifiant national d’échecs du joueur :[{first_player_id}]")
        if player_id:
            return player_id
        else:
            return first_player_id

    def print_list_of_object(self, object_list, property_list, headers = None):
        """
        Permet de print en tableau une liste d'élément avec les property contenu dans property_list
        :param object_list: liste d'objets à afficher
        :param property_list: liste de property à afficher (sert également de header au tableau)
        """
        data_to_print = []
        for obj in object_list:
            player_info = []
            for prop in property_list:
                if hasattr(obj, prop):
                    player_info.append(getattr(obj, prop))
            data_to_print.append(player_info)

        headers = headers or property_list
        print(tabulate(data_to_print, headers))





    def show_error_message(self, error_message):
        """
        Affiche un message d'erreur
        :param error_message: message à afficher
        """
        print(f"### ERREUR : {error_message} ###")
