from models.player import Player
from models.tournament import Tournament
from views.views import View
import json


class Controller:
    # def __init__(self):
    # self.view = View()
    
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
            tournament.close_round(round, i)
            tournament.actualise_players_score(i)
            print("players",tournament.players)
        
        tournament_winners = tournament.get_winner()
        View.close_tournament(tournament_winners)
    


    @staticmethod
    def register_player():
        player_info = View.register_player()
        print(player_info)
        player = Player(player_info["first_name"], player_info["last_name"], player_info["id"], player_info["date_of_birth"])
        player.register_player()




    



