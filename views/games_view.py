import datetime
from rich import print
import subprocess
import os
import sys
from utils import go_back_to_menu_or_exit_programme


class View:
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