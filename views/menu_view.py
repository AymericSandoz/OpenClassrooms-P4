import datetime
from rich import print
import subprocess
import os
import sys
from utils import go_back_to_menu_or_exit_programme


class View:
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