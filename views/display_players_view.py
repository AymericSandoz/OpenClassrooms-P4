import datetime
from rich import print
import subprocess
import os
import sys
from utils import go_back_to_menu_or_exit_programme


class View:
    @staticmethod
    def display_players(player_id, player_first_name, player_last_name, player_date_of_birth):
        print("Player ID :", player_id)
        print("Name :", player_first_name, player_last_name)
        print("Date of birth :", player_date_of_birth)
        print("[cyan]---------------------[/cyan]")    

    @staticmethod
    def display_player(player, player_tournaments):
        print("Player ID :", player["id"])
        print("Name :", player["first_name"], player["last_name"])
        print("Date of birth :", player["date_of_birth"])
        print(f"Tournaments participated by the player: ")
        for tournament in player_tournaments:
            print(f"Tournament name: {tournament['tournament_name']}")
            print(f"Player's score: {tournament['score']}")
            print('[cyan]---[/cyan]')
        print("[cyan]---------------------[/cyan]")
    
    @staticmethod
    def get_player_id(players):
        while True:
            input_ID = input("Please if your want more information on a player, enter it's ID:")
            if input_ID == "menu" or input_ID == "Menu":
                return "menu"
            pattern = r'^[A-Z]{2}\d{5}$'
            if not re.search(pattern, input_ID):
                print("[bold red]Sorry the ID format is not valid[/bold red]")
                continue
            for player in players:
                if player["id"] == input_ID:
                    return player["id"]
            print("[bold red]Sorry there is no player with this ID[/bold red]")
            continue