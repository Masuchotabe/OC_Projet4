
from src.dabatase import PlayerManager, TournamentManager
from src.views import MainView


class MainController:
    """
    Controlleur principal
    """

    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.view = MainView()
        self.selected_tournament = None

    def manage_players(self):
        while True:
            text_choices = ["Afficher tous les joueurs",
                            "Créer un joueur",
                            "Revenir au menu précédent"]
            result_choice = int(self.view.show_menu(choices=text_choices))

            match result_choice:
                case 1:
                    self.view.show_players_list(self.player_manager.players)
                case 2:
                    self.add_new_player()
                case 3:
                    break
                case _:
                    pass

    def add_new_player(self):
        player_info = self.view.prompt_for_new_player()
        self.player_manager.create_player(player_info)

    def manage_tournaments(self):
        while True:
            text_choices = ["Afficher tous les tournois",
                            "Créer un tournois",
                            "Sélectionner un  tournois",
                            "Revenir au menu précédent",
                            ]
            result_choice = int(self.view.show_menu(choices=text_choices))
            match result_choice:
                case 1:
                    self.view.show_tournaments_list(self.tournament_manager.tournaments)
                case 2:
                    self.add_new_tournament()
                case 3:
                    self.select_tournament()
                case 4:
                    break
                case _:
                    pass

    def manage_tournament(self):
        if self.selected_tournament:

            x_continue = True
            while x_continue:
                text_choices = ["Ajouter un joueur",
                                "Afficher le classement des joueurs",
                                "Reprendre" if self.selected_tournament.is_started() else "Démarrer",
                                "Revenir au menu précédent",
                                ]
                result_choice = int(self.view.show_menu(choices=text_choices))
                match result_choice:
                    case 1:
                        self.add_player_to_tournament()
                    case 2:
                        self.view.show_player_ranking()
                    case 3:
                        if not self.selected_tournament.is_started():
                            self.start_tournament()
                        elif not self.selected_tournament.is_finished():
                            pass
                        else:
                            self.view.show_error_message("Le tournois est déjà terminé.")
                    case 4:
                        x_continue = False
                    case _:
                        pass
        else:
            self.select_tournament()

    def add_new_tournament(self):
        tournament_info = self.view.prompt_for_new_tournament()
        self.tournament_manager.create_tournament(tournament_info)

    def select_tournament(self):
        result_choice = int(self.view.show_menu(choices=self.tournament_manager.tournaments))
        self.selected_tournament = self.tournament_manager.tournaments[result_choice-1]
        self.manage_tournament()

    def add_player_to_tournament(self):
        if not self.selected_tournament.is_started():
            player_id_list = [p.national_chess_identifier for p in self.selected_tournament.players]
            player_list = [p for p in self.player_manager.players if p.national_chess_identifier not in player_id_list]
            player_id = self.view.prompt_for_player_id(player_list)
            player = self.player_manager.get_player(player_id)
            self.selected_tournament.players.append(player)
            self.tournament_manager.save_tournaments()
        else:
            self.view.show_error_message("Il n'est pas possible d'ajouter un joueur après le début du tournois.")

    def run(self):
        text_choices = ["Gestion des joueurs", "Gestion des tournois", "Quitter l'application"]

        while True:
            result_choice = int(self.view.show_menu(choices=text_choices))
            match result_choice:
                case 1:
                    self.manage_players()
                case 2:
                    self.manage_tournaments()
                case 3:
                    break
                case _:
                    pass
