from models.tournament import Tournament
from models.game import Game
from views.tournaments_view import Tournament_view
from views.players_view import Player_view
from views.games_view import Games_view
import json


class Tournament_controller:

    @staticmethod
    def launch_tournament():
        "execute a tournament from the start to the end"
        Tournament_view.intro_message()
        name = Tournament_view.get_tournament_name()
        location = Tournament_view.get_tournament_location()
        tournament = Tournament(name, location)

        with open("data/players.json", 'r') as file:
            players = json.load(file)["players"]
            ids = [p["id"] for p in players]

        players = Player_view.get_players(ids)
        tournament.add_players(players)

        for round_number in range(tournament.nb_rounds):
            round = tournament.create_round()
            while not round.closed:
                Games_view.show_games(round.games, round_number)
                result = Games_view.input_result(round.games)
                if result == "closed":
                    if round.close_round(tournament.id, round_number) is False:
                        Games_view.enter_all_games()

                else:
                    score = Game.attribute_score(result["winner"])
                    Game.close_game(score, result["game_id"], tournament.id, round_number)

            tournament.actualise_players_score(round_number)

        tournament_winners = tournament.get_and_save_winners()
        tournament.close_tournament()
        Tournament_view.close_tournament(tournament_winners)

    @staticmethod
    def display_tournaments():
        "display a list of all the tournaments"
        with open('data/tournaments.json') as file:
            data = json.load(file)
        tournaments = data['tournaments']
        for tournament in tournaments:
            tournament_id = tournament.get('id', 'N/A')
            tournament_name = tournament.get('name', 'N/A')
            start_date = tournament.get('start date', 'N/A')
            end_date = tournament.get('end date', 'N/A')
            winners = tournament.get('winners', [])

            Tournament_view.display_tournaments(tournament_id, tournament_name,
                                                start_date, end_date, winners)

    @staticmethod
    def display_tournament():
        "display one tournament"
        with open("data/tournaments.json") as file:
            data = json.load(file)
        tournaments = data["tournaments"]
        tournament_id = Tournament_view.get_tournament_id(tournaments)
        if tournament_id == "menu":
            return
        for tournament in tournaments:
            if tournament["id"] == tournament_id:
                target_tournament = tournament

        target_tournament["players"].sort(key=lambda x: x["last_name"])

        Tournament_view.display_tournament(target_tournament)
