
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

    def show_players_list(self, players):
        for player in players:
            print(player)
