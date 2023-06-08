import datetime
from rich import print
import subprocess
import os
import sys
from utils import go_back_to_menu_or_exit_programme


class View:      
    @staticmethod
    def display_tournament(tournament):
        print("Tournament Name:", tournament["name"])
        print("Start Date:", tournament["start date"])
        print("Location:", tournament["location"])
        print("Description:", tournament["description"])
        print("Players:")
        for player in tournament["players"]:
            print(player["first_name"], player["last_name"], "ID:", player["id"])
        print("Rounds:")
        for round in tournament["rounds"]:
            print("Round", round["round_number"])
            for game in round["games"]:
                player1 = game[0]["player1"]
                player2 = game[1]["player2"]
                print(player1["first_name"], player1["last_name"], "vs", player2["first_name"], player2["last_name"])
                print("Score:", game[0]["score"], "-", game[1]["score"])
                print("[bold]---------------------[/bold]")
    
    @staticmethod
    def display_tournaments(tournament_id, tournament_name, start_date, end_date, winners):
        print("Tournament ID:", tournament_id)
        print("Name:", tournament_name)
        print("Start Date:", start_date)
        print("End Date:", end_date)
        if len(winners) > 1:
            print("Winners:")
            for winner in winners:
                print(winner["first_name"], winner["last_name"])
        elif winners != []:
            print("Winners:", winners[0]["first_name"], " ", winners[0]["last_name"])
        print("[cyan]---------------------[cyan]")
    
    @staticmethod
    def get_tournament_id(tournaments):
        while True:
            input_ID = input("Please if your want more information on a tournament, enter it's ID:")
            if input_ID == "menu" or input_ID == "Menu":
                return "menu"
            if (input_ID.isdigit() and len(input_ID) == 7) is not True:
                print("[bold red]Sorry the ID format is not valid[/bold red]")
                continue
            for tournament in tournaments:
                if tournament["id"] == int(input_ID):
                    return tournament["id"]
            print("[bold red]Sorry there is no tournament with this ID[/bold red]")
            continue
    