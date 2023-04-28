import random
from models.round import Round
from models.game import Game
import json
from views.views import View


class Tournament:
    def __init__(self, name, location, start_date, end_date, players=[], rounds=[], nb_rounds=4,current_round=1, description="tournoi d'échec",played_games=[]):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.rounds = rounds
        self.nb_rounds = nb_rounds
        self.description = description
        self.current_round = current_round
        self.played_games = played_games
        self.open_tournament()

    def add_players(self, players):
        self.players += players
        with open("data/players.json", 'r') as f:
            all_players = json.load(f)["players"]
            self.players = [p for p in all_players if p["id"] in self.players]

        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
        for tournament in data["tournaments"]:
            if tournament["name"] == self.name:
                tournament.update({"players": self.players})
                break
            
        with open("data/tournaments.json", "w") as f:
            json.dump(data, f)



    def open_tournament(self):
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            tournament_data = {
                "name": self.name,
                "start date": self.start_date.strftime('%Y-%m-%d'),
                "location": self.location,
                "description": self.description
            }
            data["tournaments"].append(tournament_data)
        with open("data/tournaments.json", "w") as f:
            json.dump(data, f)



    # def get_players_info(self):
    #     """Get players information by ids"""
    #     with open("data/players.json", 'r') as f:
    #         all_players = json.load(f)["players"]
    #         self.players = [p for p in all_players if p["id"] in self.players]

    def shuffle_players(self):
        random.shuffle(self.players)

    def create_round(self, start_date):
        if len(self.rounds) < self.nb_rounds: #marche que si on n'a pas dépasser le nb de rounds
            round = Round(f"{len(self.rounds) + 1}", start_date) #Round("Round {}".format(len(self.rounds) + 1), start_date)
            self.rounds.append(round)
            games = self.pair_players()
            round.add_games(games)
            return round
    
    def close_round(self, round, round_number):
        print("round :", round)
        View.show_games(round.games, round_number)
        while not round.closed:
            result = View.input_result(round.games)
            if result == "closed":
                #il faut rajoute une fonction qui analyse si tous les scores ont bien été rentrés
                round.closed = True
            else:
                Game.attribute_score(result) 

        
    
    def check_if_game_already_played(self, player1, player2):
        for game in self.played_games:
            if player1 in game and player2 in game:
                return True
        return False

    def pair_players(self):
        """return list of games"""
        games = []
        if len(self.rounds) == 1:
            self.shuffle_players()
            for i in range(0, len(self.players), 2):
                player1 = self.players[i]
                player2 = self.players[i+1]
                ##je sais pas comment faire en sorte d'utiliser une Classe Game la dessus 
                games.append(Game(player1, player2)) #la je rentre des scores égale à 0 il faut que je comprenne quand et comment les modifier
        
        else:
            print(f"round {len(self.rounds)}")  # La ou il audras trier en fonction du score
        return games
    