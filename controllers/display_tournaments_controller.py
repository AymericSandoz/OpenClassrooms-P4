  
from models.player import Player
from models.tournament import Tournament
from views.views import View
import json


class Controller:    
    
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
    