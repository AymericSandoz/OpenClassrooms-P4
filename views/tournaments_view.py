import datetime
from rich import print
from utils import go_back_to_menu_or_exit_programme

class Tournament_view:
    
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
        print(f"[bold cyan]{name}[/bold cyan] ? That's an excellent name")
        return name
    
    @staticmethod
    def get_tournament_location():
        print("Where will the [bold cyan]tournament[/bold cyan] be held ?")
        location = input("> ")
        print("Nice ! ")
        return location
    
    # @staticmethod
    # def get_tournament_start_date():
    #     while True:
    #         try: 
    #             start_date = datetime.datetime.strptime(input("When does it start ? (in DD/MM/YYYY)"),"%d/%m/%Y").date()
    #             return start_date
    #         except ValueError:
    #             print("[bold red]Invalid answer[/bold red]")
    #             continue
        
    
    # @staticmethod
    # def get_tournament_end_date(start_date):
    #     while True:
    #         try:
    #             end_date = datetime.datetime.strptime(input("And when does it finish (in DD/MM/YYYY)? "),"%d/%m/%Y").date()
    #             if (end_date >= start_date):
    #                 print("perfect !")
    #                 return start_date
    #             else:
    #                 print("[bold red]The end date has to be after the start date ![/bold red]")
    #         except ValueError:
    #             print("[bold red]Invalid answer[/bold red]")
    #             continue
  
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
  