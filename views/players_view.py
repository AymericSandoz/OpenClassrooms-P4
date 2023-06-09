from rich import print
import re

class Player_view:    
    @staticmethod
    def register_player():
        "register_player_to_the_federation"
        first_name = input("enter first name :") 
        last_name = input("enter last name :")
        id = input("enter id :")
        date_of_birth = input("enter date of birth :")
        return {"first_name": first_name, "last_name": last_name, "id": id, "date_of_birth": date_of_birth}
    
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
    def id_already_existing(id):
        print(f"[bold red]L'id {id} existe déjà.[/bold red]")

    @staticmethod
    def register_player_to_fd_success_message(first_name):
        print(f"Le joueur [bold cyan]{first_name}[/bold cyan] a été ajouté avec succès.")
    
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
