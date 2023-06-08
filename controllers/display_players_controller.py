from models.player import Player
from models.tournament import Tournament
from views.views import View
import json

class Controller:
    
    @staticmethod
    def display_players():
        with open('data/players.json') as file:
            data = json.load(file)
        players = data['players']
        for player in players:
            player_id = player.get('id', 'N/A')
            player_first_name = player.get('first_name', 'N/A')
            player_last_name = player.get('last_name', 'N/A')
            player_date_of_birth = player.get('date_of_birth', 'N/A')
            View.display_players(player_id, player_first_name, player_last_name, player_date_of_birth)
    
    @staticmethod
    def display_player():
        with open("data/players.json") as file:
            data = json.load(file)
        players = data["players"]
        player_id = View.get_player_id(players)
        if player_id == "menu":
            return 
        for player in players:
            if player["id"] == player_id:
                target_player = player

        #search player tournaments
        with open('data/tournaments.json', 'r') as file:
            data = json.load(file)

        player_tournaments = []
        tournaments = data.get('tournaments', [])
        for tournament in tournaments:
            players = tournament.get('players', [])
            for player in players:
                if player.get('id') == player_id:
                    player_tournaments.append({
                        'tournament_name': tournament.get('name', ''),
                        'score': player.get('score', 0)
                    })

        View.display_player(target_player, player_tournaments)

        

