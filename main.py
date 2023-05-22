"""Entry point."""

from models.tournament import Tournament
from controllers.controllers import Controller
from models.player import Player
from views.views import View


def main():
    start_tournament_or_register_player = View.start_tournament_or_register_player()

    if start_tournament_or_register_player == "2":
        Controller.register_player()
    elif start_tournament_or_register_player == "1":
        Controller.launch_tournament()
    else:
        View.invalid_answer()
    

if __name__ == "__main__":
    main()

