import random

from src.dabatase import PlayerManager, TournamentManager
from src.views import MainView
from src.models import Match, Round


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
                            self.manage_rounds()
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

    def start_tournament(self):
        if self.selected_tournament:
            if self.selected_tournament.actual_round == 0:
                if (len(self.selected_tournament.players) >= 4) and ((len(self.selected_tournament.players) % 2) == 0):
                    matches = self.get_random_matches()
                    new_round = Round("Tour n°1", matches)
                    self.selected_tournament.actual_round = 1
                    self.selected_tournament.start()
                    self.selected_tournament.rounds.append(new_round)
                    self.tournament_manager.save_tournaments()
                else:
                    self.view.show_error_message("Le nombre de joueur du tournoi doit être pair et supérieur à 4.")
            else:
                self.view.show_error_message("Le tournoi est déjà commencé. ")
        else:
            self.select_tournament()

    def get_random_matches(self):
        players_list = self.selected_tournament.players
        random.shuffle(players_list)
        return [Match(player_1=x, player_2=y) for x, y in zip(players_list[::2], players_list[1::2])]

    def manage_rounds(self):

        x_continue = True
        while x_continue:
            self.view.show_tournament(self.selected_tournament)
            text_choices = ["Voir les matchs d'un tour",
                            "Renseigner le résultat des matchs du tour actuel",
                            "Revenir au menu précédent",
                            ]
            result_choice = int(self.view.show_menu(choices=text_choices))
            match result_choice:
                case 1:
                    self.check_round_matches()
                case 2:
                    self.manage_actual_round()
                case 3:
                    x_continue = False
                case _:
                    pass

    def manage_actual_round(self):
        actual_round = self.selected_tournament.get_actual_round()
        self.view.show_round(actual_round)
        for match in actual_round.matches:
            if not (match.score_1 and match.score_2):
                message = "Veuillez choisir le résultat du match : "
                text_choices = [f"{match.player_1} a gagné",
                                f"{match.player_2} a gagné",
                                "Match nul",
                                "Retour"
                                ]
                result_choice = int(self.view.show_menu(message=message, choices=text_choices))
                match result_choice:
                    case 1:
                        match.score_1 = 1.0
                        match.score_2 = 0.0
                    case 2:
                        match.score_1 = 0.0
                        match.score_2 = 1.0
                    case 3:
                        match.score_1 = 0.5
                        match.score_2 = 0.5
                    case _:
                        pass
            self.tournament_manager.save_tournaments()
        self.selected_tournament.update_players_score()
        self.tournament_manager.save_tournaments()

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
