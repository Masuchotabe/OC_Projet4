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
        """
        Permet de vider le terminal
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self, choices, message=None):
        """
        Affiche un menu à l'utilisateur et retourne le choix
        :param choices: Choix à afficher
        :param message: message à afficher
        :return: nombre entier représentant le menu choisi
        """
        valid_result = False
        while not valid_result:
            if message:
                print(message)
            else:
                print("Veuillez choisir un menu :")
            for index, choice in enumerate(choices, start=1):
                print(f"{index} - {choice}")
            user_input = input("Votre choix : ")
            print('#'*50)
            if user_input.isnumeric():
                if 0 < int(user_input) <= len(choices):
                    return int(user_input)

            print(f"ERREUR : Veuillez renseigner un entier compris entre 1 et {len(choices)}")

    def prompt_for_new_player(self):
        """
        Demande les informations du nouveau joueur
        :return: dict du nouveau joueur
        """
        self.clear_console()
        print("Veuillez renseigner les informations du nouveau joueur : ")
        first_name = input("Son prénom : \n")
        last_name = input("Son nom de famille : \n")
        birth_date = input("Sa date de naissance (jj/mm/aaaa) : \n")
        national_chess_identifier = input("Son identifiant national d'échecs (AAXXXXX) : \n")
        return {'first_name': first_name,
                'last_name': last_name,
                'birth_date': birth_date,
                'national_chess_identifier': national_chess_identifier}

    def prompt_for_new_tournament(self):
        """
        Demande les informations du nouveau tournoi
        :return: dict du nouveau tournoi
        """
        self.clear_console()
        print("Veuillez renseigner les informations du nouveau tournois : ")
        name = input("Son nom : \n")
        description = input("Sa description : \n")
        location = input("Son lieu : \n")
        number_of_rounds = input("nombre de tours : \n")
        start_date = input("Sa date de début (jj/mm/aaaa) : \n")
        end_date = input("Sa date de fin (jj/mm/aaaa) : \n")

        return {'name': name,
                'description': description,
                'location': location,
                'number_of_rounds': number_of_rounds,
                'start_date': start_date,
                'end_date': end_date
                }

    def show_players_list(self, players, sort_by_last_name=True):
        """
        Permet d'afficher la liste de joueur en tableau
        :param players: Liste de joueur
        :param sort_by_last_name: Définit si les joueurs doivent être triés par last_name
        """
        self.clear_console()

        property_list = ["first_name", "last_name", "birth_date", "national_chess_identifier"]
        headers = ["Prénom", "Nom", "Date de naissance", "Identifiant national d'échecs"]
        if sort_by_last_name:
            players.sort(key=lambda player: player.last_name.lower())
        self._print_list_of_object(players, property_list, headers)

    def show_players_score(self, players_dict_list, sort_by_last_name=True):
        """
        Permet d'afficher le score et le rang des joueurs
        :param players_dict_list: Dictionnaire avec info sur les joueurs et leur score
        :param sort_by_last_name: Définit si les joueurs doivent être triés par last_name
        """
        self.clear_console()

        property_list = ["rank", "first_name", "last_name", "birth_date", "national_chess_identifier", "score"]
        headers = ["Rang", "Prénom", "Nom", "Date de naissance", "Identifiant national d'échecs", "Score"]
        if sort_by_last_name:
            players_dict_list.sort(key=lambda player: player['last_name'])
        self._print_list_of_dict(players_dict_list, property_list, headers)

    def show_tournaments_list(self, tournaments):
        """
        Permet d'afficher
        :param tournaments:
        :return:
        """
        self.clear_console()
        property_list = ["name", "location", "start_date", "end_date", "description"]
        headers = ["Nom", "Lieu", "Date de début", "Date de fin", "Description"]
        self._(tournaments, property_list, headers)

    def show_tournament(self, tournament):
        """
        Affiche le nom du tournoi et la liste de ses rounds
        :param tournament : objet Tournoi
        """
        print(f"\nTournoi {tournament.name} du {tournament.start_date} au {tournament.end_date}")
        for round in tournament.rounds:
            if round.round_number != tournament.actual_round_number:
                print(f"{round.name}")
            else:
                print(f"{round.name} - Tour actuel")

    def show_round_list(self, round_list):
        """
        Affiche la liste des rounds
        :param round_list: liste des rounds
        """
        property_list = ["name", "start_date", "end_date"]
        headers = ["Nom", "Date de début", "Date de fin"]
        self._print_list_of_object(round_list, property_list, headers)

    def show_round(self, tournament_round):
        self.clear_console()
        print(f"\n{tournament_round.name}")
        property_list = ["player_1", "score_1", "player_2", "score_2"]
        headers = ["Joueur 1", "Score 1", "Joueur 2", "Score 2"]
        self._print_list_of_object(tournament_round.matches, property_list, headers)
        # for match in tournament_round.matches:
        #
        #     print(match)

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

    def _print_list_of_object(self, object_list, property_list, headers=None):
        """
        Permet de print en tableau une liste d'élément avec les property contenu dans property_list
        :param object_list: liste d'objets à afficher
        :param property_list: liste de property à afficher (sert également de header au tableau)
        :param headers: Surcharge les en-tetes du tableau
        """
        data_to_print = []
        for obj in object_list:
            object_info = []
            for prop in property_list:
                if hasattr(obj, prop):
                    object_info.append(getattr(obj, prop))
            data_to_print.append(object_info)

        headers = headers or property_list
        print(tabulate(data_to_print, headers, stralign='center', numalign='center'))
        print("######### FIN DU TABLEAU #########")

    def _print_list_of_dict(self, dict_list, key_list, headers=None):
        """
        Permet de print en tableau une liste de dictionnaire avec les clés contenu dans key_list
        :param dict_list: liste de dictionnaire à afficher
        :param key_list: liste de clé à afficher (sert également de header au tableau)
        :param headers: Surcharge les en-tetes du tableau
        """
        data_to_print = []
        for dictionnary in dict_list:
            dictionnary_info = []
            for key in key_list:
                if key in dictionnary:
                    dictionnary_info.append(dictionnary[key])
            data_to_print.append(dictionnary_info)

        headers = headers or key_list
        print(tabulate(data_to_print, headers, stralign='center', numalign='center'))

    def show_error_message(self, error_message):
        """
        Affiche un message d'erreur
        :param error_message: message à afficher
        """
        print(f"### ERREUR : {error_message} ###")
