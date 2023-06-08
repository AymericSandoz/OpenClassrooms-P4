"""Entry point."""

from models.tournament import Tournament
from controllers.controllers import Controller
from models.player import Player
from views.views import View
import sys


def main():

    while True:#Il faudrais faire un controller menu
        menu_choice = View.menu()

        if menu_choice == "1":
            Controller.launch_tournament()
            continue
        elif menu_choice == "2":
            Controller.register_player()
            continue
        elif menu_choice == "3":
            Controller.display_tournaments()
            Controller.display_tournament()
            continue
        elif menu_choice == "4":
            Controller.display_player()
            continue
        elif menu_choice == "5":
            View.goodbye()
            sys.exit()
            break


    
if __name__ == "__main__":
    main()

