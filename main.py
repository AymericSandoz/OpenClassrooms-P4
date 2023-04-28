"""Entry point."""

from models.tournament import Tournament
from controllers.controllers import Controller
from models.player import Player
from views.views import View


def main():
    start_tournament_or_register_player = View.start_tournament_or_register_player()

    if start_tournament_or_register_player == "2":
        player_info = View.register_player()
        print(player_info)
        player = Player(player_info["first_name"], player_info["last_name"], player_info["id"], player_info["date_of_birth"])
        player.register_player()
    elif start_tournament_or_register_player == "1":
        Controller.start_tournament()
    else:
        View.invalid_answer()
    

if __name__ == "__main__":
    main()

