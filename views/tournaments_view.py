import datetime
from rich import print
import subprocess
import os
import sys
from utils import go_back_to_menu_or_exit_programme


class View:
    
    @staticmethod
    def intro_message():
        print("Hello, Welcome to our [bold cyan]tournament[/bold cyan]")
        print("The number of [bold cyan]players[/bold cyan] must be [bold cyan]even[/bold cyan]")


    @staticmethod
    def goodbye():
        print("[bold]Goodbye[/bold]")

    @staticmethod
    def get_tournament_name():
        print("How would you like to call your [bold cyan]tournament[/bold cyan] ?")
        name = input("> ")
        go_back_to_menu_or_exit_programme(name)
        print(f"[bold cyan]{name}[/bold cyan] ? That's an excellent name")
        return name
    
    @staticmethod
    def get_tournament_location():
        print("Where will the [bold cyan]tournament[/bold cyan] be held ?")
        location = input("> ")
        print("Nice ! ")
        return location
    
    @staticmethod
    def get_tournament_start_date():
        while True:
            try: 
                start_date = datetime.datetime.strptime(input("When does it start ? (in DD/MM/YYYY)"),"%d/%m/%Y").date()
                return start_date
            except ValueError:
                print("[bold red]Invalid answer[/bold red]")
                continue
        
    
    @staticmethod
    def get_tournament_end_date(start_date):
        while True:
            try:
                end_date = datetime.datetime.strptime(input("And when does it finish (in DD/MM/YYYY)? "),"%d/%m/%Y").date()
                if (end_date >= start_date):
                    print("perfect !")
                    return start_date
                else:
                    print("[bold red]The end date has to be after the start date ![/bold red]")
            except ValueError:
                print("[bold red]Invalid answer[/bold red]")
                continue

    @staticmethod
    def get_players(players_ids):
        "register player to tournament"
        print("It's now time to register players")
        while True:
            print("[bold]Do you want to add manually players or choose a list of preregistered players?[/bold]")
            print("[cyan]1.[/cyan] Add manually players")
            print("[cyan]2.[/cyan] Choose a list of preregistered players")
            reponse = input("> ")
            players = []
            if reponse == "1":
                while True:
                    id = input("Please enter player's id. (or enter 'exit' to stop) : ")
                    if id == "exit":
                        if len(players) % 2 == 0:
                            break
                        else:
                            print("The number of player must be even")
                    elif id in players:
                        print(f"[bold red]{id} has already been added.[/bold red]")
                    elif id not in players_ids:
                        print(f"[bold red]{id} not registered in our list of player.[/bold red]")
                    else:
                        players.append((id))
            elif reponse == "2":
                players.extend(["YR27653", "YR34681", "DT91027", "TF52376", "CT83941", "KX57234", "LE65874", "ZD22348"])#permet d'ajouter les éléments directement dans la liste [] au lieu de les impriquer
            else:
                print("[bold red]Invalid answer[/bold red]")
                continue
            
            return players
    
    @staticmethod
    def close_tournament(tournament_winners):
        print('[bold]Thanks, the tournament is over[bold]')

        if len(tournament_winners) == 1:
            winner = tournament_winners[0]
            print(f"Congratulation to [bold cyan]{winner['first_name']} {winner['last_name']}[/bold cyan] who won the tournament with a score of {winner['score']}")
        else:
            print("Congratulation to")
            for player in tournament_winners:
                print(f"[bold cyan]{player['first_name']} {player['last_name']}[/bold cyan],")
            print(f"who won the tournament with a score of [bold cyan]{player['score']}[bold cyan]")
    
    @staticmethod
    def no_player_found(id):
        print(f"[bold red]Aucun joueur avec l'ID {id} n'a été trouvé.[/bold red]")
  