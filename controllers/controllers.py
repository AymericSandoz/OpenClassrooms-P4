from models.player import Player
from models.tournament import Tournament
from views.views import View
import json


class Controller:
    
    @staticmethod
    def launch_tournament():
        View.intro_message()
        name = View.get_tournament_name()
        location = View.get_tournament_location()
        start_date = View.get_tournament_start_date()
        end_date = View.get_tournament_end_date(start_date)

        tournament = Tournament(name, location, start_date, end_date)

        with open("data/players.json", 'r') as file:#une ressource. Plus performant grace à with. Optimisation de la mémoire. Exexute u dispose une foois with terminée. 
            players = json.load(file)["players"]#récupère un dictionnaire 
            ids = [p["id"] for p in players]#compréhension de liste 
            
        players = View.get_players(ids)
        tournament.add_players(players)

        for i in range(tournament.nb_rounds):
            round = tournament.create_round("30/10/2020") #attention ensuite il faut que les dates se remplisse automatiquement mais pas bien compris comment ? Est ce qu'il faut que la date du jour soit uatomatiquement utilisée comme start_date 
            while not round.closed:
                View.show_games(round.games, i)
                result = View.input_result(round.games)
                tournament.close_round(round, i, result)
            tournament.actualise_players_score(i)
        
        tournament_winners = tournament.get_and_save_winners()
        View.close_tournament(tournament_winners)
    


    @staticmethod
    def register_player():
        player_info = View.register_player()
        player = Player(player_info["first_name"], player_info["last_name"], player_info["id"], player_info["date_of_birth"])
        success_message = player.register_player()
        if success_message == "echec":
            View.id_already_existing(player.id)
        else:
            View.register_player_to_fd_success_message(player.id)
    
    @staticmethod
    def display_tournaments():
        with open('data/tournaments.json') as file:
            data = json.load(file)
        tournaments = data['tournaments']
        for tournament in tournaments:
            tournament_id = tournament.get('id', 'N/A')
            tournament_name = tournament.get('name', 'N/A')
            start_date = tournament.get('start date', 'N/A')
            end_date = tournament.get('end date', 'N/A')
            winners = tournament.get('winners', [])

            View.display_tournaments(tournament_id, tournament_name, start_date, end_date, winners)
    
    @staticmethod
    def display_tournament():
        with open("data/tournaments.json") as file:
            data = json.load(file)
        tournaments = data["tournaments"]
        tournament_id = View.get_tournament_id(tournaments)
        if tournament_id == "menu":
            return 
        for tournament in tournaments:
            if tournament["id"] == tournament_id:
                target_tournament = tournament
        View.display_tournament(target_tournament)
    
    @staticmethod
    def display_player():
        with open('data/players.json') as file:
            data = json.load(file)
        players = data['players']
        for player in players:
            player_id = player.get('id', 'N/A')
            player_first_name = player.get('name', 'N/A')
            player_last_name = player.get('start date', 'N/A')
            player_date_of_birth = player.get('date_of_birth', 'N/A')
            View.display_player(player_id, player_first_name, player_last_name, player_date_of_birth)
        

        





    



