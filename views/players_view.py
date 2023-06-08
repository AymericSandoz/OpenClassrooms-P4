import datetime
from rich import print
import subprocess
import os
import sys
from utils import go_back_to_menu_or_exit_programme


class View:    
    @staticmethod
    def register_player():
        "register_player_to_the_federation"
        first_name = input("enter first name :") 
        last_name = input("enter last name :")
        id = input("enter id :")
        date_of_birth = input("enter date of birth :")
        return {"first_name": first_name, "last_name": last_name, "id": id, "date_of_birth": date_of_birth}

    @staticmethod
    def id_already_existing(id):
        print(f"[bold red]L'id {id} existe déjà.[/bold red]")

    @staticmethod
    def register_player_to_fd_success_message(first_name):
        print(f"Le joueur [bold cyan]{first_name}[/bold cyan] a été ajouté avec succès.")
