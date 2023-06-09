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