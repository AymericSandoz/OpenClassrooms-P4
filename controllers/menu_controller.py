from views.menu_view import Menu_view
from controllers.tournament_controller import Tournament_controller
from controllers.player_controller import Player_controller
import os
import sys


class Menu_controller:

    @staticmethod
    def menu():
        while True:
            menu_choice = Menu_view.menu()
            if menu_choice == "1":
                Tournament_controller.launch_tournament()
                continue
            elif menu_choice == "2":
                Player_controller.register_player()
                continue
            elif menu_choice == "3":
                Tournament_controller.display_tournaments()
                Tournament_controller.display_tournament()
                continue
            elif menu_choice == "4":
                Player_controller.display_players()
                Player_controller.display_player()
                continue
            elif menu_choice == "5":
                os.system('cls')
                sys.exit()



