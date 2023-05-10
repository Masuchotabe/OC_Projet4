
from src.dabatase import PlayerManager
from src.views import MainView


class MainController:
    """
    Controlleur principal
    """

    def __init__(self):
        self.player_manager = PlayerManager()
        self.view = MainView()

    def manage_players(self):
        text_choices = ["Afficher tous les joueurs",
                        "Ajouter un joueur",
                        "Revenir au menu précédent"]
        result_choice = int(self.view.show_menu(choices=text_choices))

        match result_choice:
            case 1:
                self.view.show_players_list(self.player_manager.players)
            case 2:
                self.add_new_player()
            case _:
                pass

    def add_new_player(self):
        player_info = self.view.prompt_for_new_player()
        self.player_manager.create_player(player_info)

    def run(self):
        text_choices = ["Gestion des joueurs", "Gestion des tournois", "Quitter l'application"]

        while True:
            result_choice = int(self.view.show_menu(choices=text_choices))
            match result_choice:
                case 1:
                    self.manage_players()
                case 2:
                    pass
                case 3:
                    break
                case _:
                    pass



