import os
import sys
import json

def go_back_to_menu_or_exit_programme(user_input):
    if user_input.lower() == "menu":
        os.system('cls' if os.name == 'nt' else 'clear') 
        return 'menu'

    if user_input.lower() == "exit":
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()

def search_tournaments_by_player(player_id):
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

        return player_tournaments