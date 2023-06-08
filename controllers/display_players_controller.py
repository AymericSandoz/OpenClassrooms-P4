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
            player_first_name = player.get('name', 'N/A')
            player_last_name = player.get('start date', 'N/A')
            player_date_of_birth = player.get('date_of_birth', 'N/A')
            View.display_player(player_id, player_first_name, player_last_name, player_date_of_birth)
        
