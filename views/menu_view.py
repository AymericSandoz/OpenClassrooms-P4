from rich import print


class Menu_view:
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