import random
from itertools import combinations

from dabatase import PlayerManager, TournamentManager
from views.views import MainView
from models.matches import Match
from models.rounds import Round


from validators import validate_date_from_str, validate_national_chess_identifier


class MainController:
    """
    Controlleur principal du jeu
    """

    def __init__(self):
        """
        Initialise le controlleur principal avec un player manager, un tournament manager et une vue
        La variable selected_tournament permet de savoir quel tournoi on est en train de gérer
        Go_home permet de revenir à l'acceuil depuis n'importe quel menu.
        """
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.view = MainView()
        self.selected_tournament = None
        self.go_home = False

    def main_menu(self):
        """
        Menu principal de l'application.
        :return:
        """
        text_choices = ["Gestion des joueurs",
                        "Gestion des tournois",
                        "Quitter l'application",
                        ]
        while True:
            if self.selected_tournament:
                self.selected_tournament = None
            if self.go_home:
                self.go_home = False

            result_choice = int(self.view.show_menu(choices=text_choices))
            match result_choice:
                case 1:
                    self.manage_players()
                case 2:
                    self.manage_tournaments()
                case 3:
                    self.player_manager.save_players()
                    self.tournament_manager.save_tournaments()
                    break
                case _:
                    pass

    def manage_players(self):
        """
        Gère le menu concernant la partie Joueur de l'application
        """
        while True and not self.go_home:
            text_choices = ["Afficher tous les joueurs",
                            "Créer un joueur",
                            "Revenir au menu précédent",
                            "Revenir à l'accueil",
                            ]
            result_choice = int(self.view.show_menu(choices=text_choices))

            match result_choice:
                case 1:
                    self.view.show_players_list(self.player_manager.players)
                case 2:
                    self.add_new_player()
                case 3:
                    break
                case 4:
                    self.go_home = True
                case _:
                    pass

    def manage_tournaments(self):
        """
        Gère le menu concernant la partie tournoi de l'application
        """
        x_continue = True
        while x_continue and not self.go_home:
            text_choices = ["Afficher tous les tournois",
                            "Créer un tournoi",
                            "Gérer un  tournoi",
                            "Revenir au menu précédent",
                            "Revenir à l'accueil",
                            ]
            result_choice = int(self.view.show_menu(choices=text_choices))
            match result_choice:
                case 1:
                    self.view.show_tournaments_list(self.tournament_manager.tournaments)
                case 2:
                    self.add_new_tournament()
                case 3:
                    if len(self.tournament_manager.tournaments) > 0:
                        self.select_tournament()
                        self.manage_tournament()
                    else:
                        self.view.show_error_message(
                            "Il n'y a aucun tournoi dans la base. Veuillez créer un tournoi pour commencer"
                        )
                case 4:
                    x_continue = False
                case 5:
                    self.go_home = True
                case _:
                    pass

    def manage_tournament(self):
        """
        Gère la gestion d'un tournoi en fonction de son état (non commencé, en cours, fini)
        """
        x_continue = True
        while x_continue and not self.go_home:
            if not (self.selected_tournament.is_started() or self.selected_tournament.is_finished()):
                x_continue = self.manage_not_start_tournament()
            elif self.selected_tournament.is_finished():
                x_continue = self.manage_finished_tournament()
            else:
                x_continue = self.manage_in_progress_tournament()

    def manage_not_start_tournament(self):
        """
        Gestion du tournoi non commencé
        :return: True si on reste sur la gestion du tournoi, False si on veut revenir au menu précédent
        """
        text_choices = ["Ajouter un joueur",
                        "Voir la liste des joueurs",
                        "Démarrer",
                        "Revenir au menu précédent",
                        "Revenir à l'accueil",
                        ]
        result_choice = int(self.view.show_menu(choices=text_choices))
        match result_choice:
            case 1:
                if self.player_manager.players:
                    self.add_player_to_tournament()
                else:
                    self.view.show_error_message(
                        "Aucun joueur n'est présent dans la base. Veuillez d'abord ajouter des joueurs dans la base."
                    )
            case 2:
                self.view.show_players_list(self.selected_tournament.players)
            case 3:
                self.start_tournament()
            case 4:
                return False
            case 5:
                self.go_home = True
            case _:
                pass
        return True

    def manage_in_progress_tournament(self):
        """
        Gestion d'un tournoi en cours
        :return: True si on reste sur la gestion du tournoi, False si on veut revenir au menu précédent
        """
        actual_round = self.selected_tournament.get_actual_round()
        text_choices = [
            "Gérer les tours",
            f"Renseigner les résultats : {actual_round.name}" if not actual_round.is_finished()
            else "Démarrer le tour suivant",
            "Classement des joueurs",
            "Voir la liste des tours",
            "Voir les matchs d'un tour",
            "Revenir au menu précédent",
            "Revenir à l'accueil",
        ]
        result_choice = int(self.view.show_menu(choices=text_choices))
        match result_choice:
            case 1:
                self.manage_rounds()
            case 2:
                if not actual_round.is_finished():
                    self.manage_actual_round()
                else:
                    self.generate_next_round()
            case 3:
                player_dict_list = self.selected_tournament.get_ranked_player_list()
                self.view.show_players_score(player_dict_list, sort_by_last_name=False)
            case 4:
                self.view.show_round_list(self.selected_tournament.rounds)
            case 5:
                self.view_round()
            case 6:
                return False
            case 7:
                self.go_home = True
            case _:
                pass
        return True

    def manage_finished_tournament(self):
        """
        Gestion d'un tournoi terminé
        :return: True si on reste sur la gestion du tournoi, False si on veut revenir au menu précédent
        """
        text_choices = ["Voir la liste des joueurs",
                        "Classement des joueurs",
                        "Voir la liste des tours",
                        "Voir les matchs d'un tour",
                        "Revenir au menu précédent",
                        "Revenir à l'accueil",
                        ]
        result_choice = int(self.view.show_menu(choices=text_choices))
        match result_choice:
            case 1:
                self.view.show_players_list(self.selected_tournament.players)
            case 2:
                player_dict_list = self.selected_tournament.get_ranked_player_list()
                self.view.show_players_score(player_dict_list, sort_by_last_name=False)
            case 3:
                self.view.show_round_list(self.selected_tournament.rounds)
            case 4:
                self.view_round()
            case 5:
                return False
            case 6:
                self.go_home = True
            case _:
                pass
        return True

    def manage_rounds(self):
        """
        Gestion des rounds (résultats, liste de match ...)
        """
        x_continue = True
        while x_continue and not self.go_home:
            self.view.show_tournament(self.selected_tournament)
            actual_round = self.selected_tournament.get_actual_round()
            text_choices = [
                "Voir les matchs d'un tour",
                ("Renseigner le résultat des matchs du tour actuel" if not actual_round.is_finished()
                 else "Démarrer le tour suivant"),
                "Revenir au menu précédent",
                "Revenir à l'accueil",
            ]
            result_choice = int(self.view.show_menu(choices=text_choices))
            match result_choice:
                case 1:
                    self.view_round()
                case 2:
                    if not actual_round.is_finished():
                        self.manage_actual_round()
                    else:
                        self.generate_next_round()
                case 3:
                    x_continue = False
                case 4:
                    self.go_home = True
                case _:
                    pass

    def view_round(self):
        """
        Affiche le détail d'un round
        """
        message = "Veuillez choisir un tour dans la liste par son numéro : "
        result_choice = int(self.view.show_menu(choices=self.selected_tournament.rounds, message=message))
        self.view.show_round(self.selected_tournament.rounds[result_choice - 1])

    def manage_actual_round(self):
        """
        Permet de renseigner les résultats des matchs en cours. Enregistre les résultats et met à jour les scores.
        """
        actual_round = self.selected_tournament.get_actual_round()
        self.view.show_round(actual_round)
        for match in actual_round.matches:
            if not match.has_result():
                message = f"Veuillez choisir le résultat du match {match.player_1} VS {match.player_2} : "
                text_choices = [f"{match.player_1} a gagné",
                                f"{match.player_2} a gagné",
                                "Match nul",
                                "Match suivant"
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
        if actual_round.are_all_match_results_complete():  # si tous les matchs sont complétés on termine le round
            actual_round.finish()
            player_dict_list = self.selected_tournament.get_ranked_player_list()  # et on affiche le classement
            self.view.show_players_score(player_dict_list, sort_by_last_name=False)

        self.tournament_manager.save_tournaments()

    def add_new_tournament(self):
        """
        Permet d'ajouter un nouveau tournoi et vérifie si les données sont valides
        """
        tournament_data = self.view.prompt_for_new_tournament()
        if self.validate_tournament_data(tournament_data):
            self.tournament_manager.create_tournament(tournament_data)
        else:
            self.view.show_error_message("La création a échouée. Veuillez réessayer.")

    def validate_tournament_data(self, tournament_data):
        """
        Valide les données du tournoi
        :param tournament_data : Données du tournoi
        :return: True si les données sont valides
        """
        data_valid = True
        if isinstance(tournament_data, dict):
            if not (
                tournament_data['number_of_rounds']
                and tournament_data['name']
                and tournament_data['location']
                and tournament_data['start_date']
                and tournament_data['end_date']
            ):
                self.view.show_error_message("Veuillez compléter tous les champs obligatoires")
            if isinstance(tournament_data['number_of_rounds'], int):
                if not tournament_data['number_of_rounds'] > 0:
                    self.view.show_error_message("Le nombre de tours doit être un entier supérieur à 0.")
                    data_valid = False
            elif isinstance(tournament_data['number_of_rounds'], str):
                if not all(c.isdigit() for c in tournament_data['number_of_rounds']):
                    self.view.show_error_message("Le nombre de tours doit être un entier positifs.")
                    data_valid = False
            elif tournament_data['number_of_rounds'] is None:
                self.view.show_error_message("Le nombre de tours doit être renseigné.")
                data_valid = False
            if not (validate_date_from_str(tournament_data['start_date']) or validate_date_from_str('end_date')):
                self.view.show_error_message("Les dates doivent être au format JJ/MM/AAAA.")
                data_valid = False
        else:
            self.view.show_error_message("Le type de donnée attendu n'est pas respecté. Contacter le développeur. ")
            data_valid = False
        return data_valid

    def start_tournament(self):
        """
        Démarre le tournoi sélectionné si c'est possible.
        :return:
        """
        if self.selected_tournament.actual_round_number == 0:
            if self.selected_tournament.can_start():
                self.generate_next_round()
            else:
                if self.selected_tournament.number_of_rounds % 2 == 0:
                    min_player_number = self.selected_tournament.number_of_rounds + 2
                else:
                    min_player_number = self.selected_tournament.number_of_rounds + 1

                self.view.show_error_message(
                    f"Le tournoi ne peut pas démarrer. Ces prérequis sont nécessaires : \n"
                    f"\t - Le nombre de joueur doit être pair.\n"
                    f"\t - Le nombre de tour doit être cohérent avec le nombre de joueur.\n"
                    f"Pour {self.selected_tournament.number_of_rounds} tours, il faut au minimum "
                    f"{min_player_number } joueurs. \n"
                )
        else:
            self.view.show_error_message("Le tournoi est déjà commencé.")

    def add_new_player(self):
        """
        Gère la création d'un nouveau joueur
        """
        player_data = self.view.prompt_for_new_player()
        if self.validate_player_data(player_data):
            self.player_manager.create_player(player_data)
        else:
            self.view.show_error_message("La création a échouée. Veuillez réessayer.")

    def validate_player_data(self, player_data):
        """
        Valide les données d'un joueur
        :param player_data: données du joueur
        :return: True si les données sont valides
        """
        data_valid = True
        if isinstance(player_data, dict):
            if not all(value for value in player_data.values()):
                self.view.show_error_message("Veuillez compléter tous les champs obligatoires")

            if self.player_manager.get_player(player_data['national_chess_identifier']):
                self.view.show_error_message(
                    f"Le numéro national d'échec {player_data['national_chess_identifier']} est déjà utilisé sur"
                    f" le joueur {self.player_manager.get_player(player_data['national_chess_identifier'])}."
                )
            if not validate_national_chess_identifier(player_data["national_chess_identifier"]):
                self.view.show_error_message(
                    "Le numéro national d'échec doit être de la forme \"AAXXXXX\" ( A = Lettre, X = Chiffre )."
                )
                data_valid = False
            if not validate_date_from_str(player_data["birth_date"]):
                self.view.show_error_message(
                    "La date de naissance doit être au format JJ/MM/AAAA."
                )
                data_valid = False

            return data_valid

    def add_player_to_tournament(self):
        """
        Sélection et ajout d'un joueur par son identifiant national d'échec (INE) dans un tournoi.
        Par défaut, le INE du premier joueur de la liste sera ajouté. Ne propose que les joueurs non présents
        dans le tournoi
        """
        if not self.selected_tournament.is_started():
            player_id_list = [p.national_chess_identifier for p in self.selected_tournament.players]
            player_list = [p for p in self.player_manager.players if p.national_chess_identifier not in player_id_list]
            player_id = self.view.prompt_for_player_id(player_list)
            player = self.player_manager.get_player(player_id)
            self.selected_tournament.players.append(player)
            self.tournament_manager.save_tournaments()
        else:
            self.view.show_error_message("Il n'est pas possible d'ajouter un joueur après le début du tournois.")

    def generate_next_round(self):
        """
        Permet de créer le round suivant du tournoi
        """
        if not self.selected_tournament.is_finished():
            new_matches = self.get_new_matches()
            actual_round = self.selected_tournament.get_actual_round()
            if actual_round:
                next_round_number = actual_round.round_number + 1
            else:
                next_round_number = 1
            round_name = f"Tour n°{next_round_number}"
            new_round = Round(name=round_name, round_number=next_round_number, matches=new_matches)

            self.selected_tournament.rounds.append(new_round)
            self.selected_tournament.actual_round_number = next_round_number
            self.tournament_manager.save_tournaments()
            self.view.show_round(new_round)
        else:
            self.view.show_error_message("Le tournoi est déjà terminé")

    def get_new_matches(self):
        """
        Récupère les matchs générés en fcontion de l'état du tournoi
        """
        if self.selected_tournament.is_started():
            new_matches = self.generate_ordered_match()
        else:
            new_matches = self.generate_random_match()
        return new_matches

    def generate_ordered_match(self):
        """
        Génère les matchs en fonction du classement des joueurs et des matchs déjà joués.
        Il n'est pas possible de générer un match ayant déjà été joué. (deux joueurs se rencontrent une seule fois)
        :return: Liste des nouveaux matchs
        """
        ordered_player_list = self.selected_tournament.get_ordered_player_list()
        possible_match = [Match(e[0], e[1]) for e in combinations(ordered_player_list, 2)
                          if not Match(e[0], e[1]) in self.selected_tournament.matches]
        new_matches = []
        player_already_selected = []
        while (len(new_matches) < int(len(self.selected_tournament.players) / 2)) and len(possible_match) > 0:
            new_match = possible_match.pop()
            if (new_match.player_1 not in player_already_selected and
                    new_match.player_2 not in player_already_selected):
                new_matches.append(new_match)
                player_already_selected.append(new_match.player_1)
                player_already_selected.append(new_match.player_2)
        return new_matches

    def generate_random_match(self):
        """
        Génère des matchs de manière aléatoire.
        :return: Liste des nouveaux matchs
        """
        players_list = self.selected_tournament.players
        random.shuffle(players_list)
        return [Match(player_1=x, player_2=y) for x, y in zip(players_list[::2], players_list[1::2])]

    def select_tournament(self):
        """
        Permet de sélectionner le tournoi à gérer
        """
        message = "Veuillez choisir un tournoi dans la liste par son id : "
        result_choice = int(self.view.show_menu(choices=self.tournament_manager.tournaments, message=message))
        self.selected_tournament = self.tournament_manager.tournaments[result_choice-1]

    def run(self):
        self.main_menu()
