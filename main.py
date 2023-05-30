"""Entry point."""

from models.tournament import Tournament
from controllers.controllers import Controller
from models.player import Player
from views.views import View


def main():
    menu_choice = View.menu()

    if menu_choice == "2":
        Controller.register_player()
    elif menu_choice == "1":
        Controller.launch_tournament()
    elif menu_choice == "3":
        Controller.display_tournaments()
        Controller.display_tournament()
    
if __name__ == "__main__":
    main()

