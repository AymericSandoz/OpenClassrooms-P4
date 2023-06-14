from rich import print


class Games_view:
    @staticmethod
    def input_result(games):
        while True:
            print("[bold]Choose a game (enter the game ID).[/bold]")
            print("[bold]If you want to close the round, enter [cyan]'closed'[/cyan] "
                  "(all scores must be added first): [/bold]")

            result_input = input("> ")
            if result_input == "closed":
                return "closed"

            try:
                if int(result_input) in list(range(len(games))):
                    game_id = int(result_input)
                    game = games[game_id]
                    print(f"[cyan]ID {game_id}:"
                          f"[/cyan] [bold]{game.player_a['first_name']} {game.player_a['last_name']}[/bold] "
                          f"VS [bold]{game.player_b['first_name']} {game.player_b['last_name']}[/bold]")
                    winner = input("Maintenant, saisissez le gagnant : A, B ou D pour un match nul : ")
                    if winner not in ["A", "B", "D"]:
                        print("[bold red]Entrée invalides, vous devez saisir A,B ou D[/bold red]")
                        continue
                    return {"winner": winner, "game_id": game_id}

                else:
                    print("[bold red]Entrée invalide."
                          "Veuillez saisir 'closed' pour clôturer la manche ou un nombre valide.[/bold red]")
                    continue
            except ValueError:
                print("[bold red]Entrée invalide."
                      "Veuillez saisir 'closed' pour clôturer la manche ou un nombre valide.[/bold red]")
                continue

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
