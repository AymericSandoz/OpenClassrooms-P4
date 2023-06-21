from models.player import Player
from views.players_view import Player_view
import json


class Player_controller:
    @staticmethod
    def register_player():
        """register player to the federation"""
        player_info = Player_view.register_player()
        player = Player(player_info["first_name"], player_info["last_name"], player_info["date_of_birth"])
        print(player)
        success_message = player.register_player()
        if success_message == "echec":
            Player_view.id_already_existing(player.id)
        else:
            Player_view.register_player_to_fd_success_message(player.id)

    @staticmethod
    def display_players():
        """display a list of all the players"""
        with open('data/players.json') as file:
            data = json.load(file)
        players = data['players']
        for player in players:
            player_id = player.get('id', 'N/A')
            player_first_name = player.get('first_name', 'N/A')
            player_last_name = player.get('last_name', 'N/A')
            player_date_of_birth = player.get('date_of_birth', 'N/A')
            Player_view.display_players(player_id, player_first_name,
                                        player_last_name, player_date_of_birth)

    @staticmethod
    def display_player():
        """display one player"""
        with open("data/players.json") as file:
            data = json.load(file)
        players = data["players"]
        player_id = Player_view.get_player_id(players)
        if player_id == "menu":
            return
        for player in players:
            if player["id"] == player_id:
                target_player = player

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

        Player_view.display_player(target_player, player_tournaments)
