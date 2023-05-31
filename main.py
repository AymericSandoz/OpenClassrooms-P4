"""Entry point."""

from models.tournament import Tournament
from controllers.controllers import Controller
from models.player import Player
from views.views import View


def main():

    while True:
        menu_choice = View.menu()

        if menu_choice == "2":
            Controller.register_player()
            continue
        elif menu_choice == "1":
            Controller.launch_tournament()
            continue
        elif menu_choice == "3":
            Controller.display_tournaments()
            Controller.display_tournament()
            continue
        elif menu_choice == "4":
            View.goodbye()
            break
    
if __name__ == "__main__":
    main()

