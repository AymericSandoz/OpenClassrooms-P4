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
    def menu():
        while True:
            print("[bold]Do you want to?[/bold]")
            print("[cyan]1.[/cyan] Start a tournament")
            print("[cyan]2.[/cyan] Register players")
            print("[cyan]3.[/cyan] Look at older tournament")
            print("[cyan]4.[/cyan] Look for players")
            print("[cyan]5.[/cyan] Exit ")
            response = input("> ")
            if response not in ["1", "2", "3", "4", "5"]:
                print("[bold red]Invalid answer[/bold red]")
                continue
            return response 
    
    @staticmethod
    def register_player():
        "register_player_to_the_federation"
        first_name = input("enter first name :") 
        last_name = input("enter last name :")
        id = input("enter id :")
        date_of_birth = input("enter date of birth :")
        return {"first_name": first_name, "last_name": last_name, "id": id, "date_of_birth": date_of_birth}

    @staticmethod
    def show_games(games, round_number):
        print(f"Hello, here are the games for round n{round_number} :")
        print("One you have entered all the scores next round will be launched : ")
        i = 0
        for game in games:
            player_a_name = f"{game.player_a['first_name']} {game.player_a['last_name']}"
            player_b_name = f"{game.player_b['first_name']} {game.player_b['last_name']}"
            print(f"ID {i}:  [bold]{player_a_name}[/bold] VS [bold]{player_b_name}[/bold]")
            i += 1

    @staticmethod
    def input_result(games):
        while True:
            print("[bold]Choose a game (enter the game ID). If you want to close the round, enter [cyan]'closed'[/cyan] (all scores must be added first): [/bold]") 
            result_input = input("> ")  
            if result_input == "closed":
                return "closed"
    
            try: 
                if int(result_input) in list(range(len(games))):
                    game_id = int(result_input)
                    game = games[game_id]
                    print(f"[cyan]ID {game_id}: [/cyan] [bold]{game.player_a['first_name']} {game.player_a['last_name']}[/bold] VS [bold]{game.player_b['first_name']} {game.player_b['last_name']}[/bold]")
                    winner = input("Maintenant, saisissez le gagnant : A, B ou D pour un match nul : ")
                    if winner not in ["A", "B", "D"]:
                        print("[bold red]Entrée invalides, vous devez saisir A,B ou D[/bold red]")
                        continue
                    return {"winner": winner, "game_id": game_id}
        
                else:
                    print("[bold red]Entrée invalide. Veuillez saisir 'closed' pour clôturer la manche ou un nombre valide.[/bold red]")
                    continue
            except:
                print("[bold red]Entrée invalide. Veuillez saisir 'closed' pour clôturer la manche ou un nombre valide.[/bold red]")
                continue
    
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
    def id_already_existing(id):
        print(f"[bold red]L'id {id} existe déjà.[/bold red]")

    @staticmethod
    def register_player_to_fd_success_message(first_name):
        print(f"Le joueur [bold cyan]{first_name}[/bold cyan] a été ajouté avec succès.")

    @staticmethod
    def no_player_found(id):
        print(f"[bold red]Aucun joueur avec l'ID {id} n'a été trouvé.[/bold red]")
    
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
    def display_players(player_id, player_first_name, player_last_name, player_date_of_birth):
        print("Player ID :", player_id)
        print("Name :", player_first_name, player_last_name)
        print("Date of birth :", player_date_of_birth)
        print("[cyan]---------------------[/cyan]")

        


       

