from models.player import Player
from models.tournament import Tournament
from views.views import View
import json


class Controller:
    def __init__(self):
        self.view = View()
  
    def start_tournament(self):
        self.view.intro_message()
        name = self.view.get_tournament_name()
        location = self.view.get_tournament_location()
        start_date = self.view.get_tournament_start_date()
        end_date = self.view.get_tournament_end_date()

        self.tournament = Tournament(name, location, start_date, end_date)

        with open("data/players.json", 'r') as f:
            players = json.load(f)["players"]
            ids = [p["id"] for p in players]
            
        players = self.view.get_players(ids)
        self.tournament.add_players(players)
        print(self.tournament.players)

    def add_players(self):
        print("addplayers")

    



