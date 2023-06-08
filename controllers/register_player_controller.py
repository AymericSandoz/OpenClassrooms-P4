  
from models.player import Player
from models.tournament import Tournament
from views.views import View
import json


class Controller:
    @staticmethod
    def register_player():
        player_info = View.register_player()
        player = Player(player_info["first_name"], player_info["last_name"], player_info["id"], player_info["date_of_birth"])
        success_message = player.register_player()
        if success_message == "echec":
            View.id_already_existing(player.id)
        else:
            View.register_player_to_fd_success_message(player.id)