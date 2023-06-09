import random
from models.round import Round
from models.game import Game
import json
from datetime import datetime


class Tournament:
    def __init__(self, name, location):
        self.id = random.randint(1000000, 9999999)
        self.name = name
        self.location = location
        self.start_date = datetime.now()
        self.players = []
        self.rounds = []
        self.nb_rounds = 4
        self.played_games = []
        self.open_tournament()
        self.winners = "unknown"

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
            print(self.start_date)
            tournament_data = {
                "id": self.id,
                "name": self.name,
                "start date": self.start_date.strftime("%Y-%m-%d %H:%M"),
                "location": self.location
            }
            data["tournaments"].append(tournament_data)
        with open("data/tournaments.json", "w") as f:
            json.dump(data, f)

    def create_round(self):
        if len(self.rounds) < self.nb_rounds:
            round = Round(f"{len(self.rounds) + 1}")
            self.rounds.append(round)
            games = self.pair_players()
            round.add_games(games, self.id, len(self.rounds))
            return round
    
    def close_round(self, round, round_number, result):
        if result == "closed":
            round.close_round(self.id, round_number)
        else:
            score = Game.attribute_score(result["winner"])
            Game.close_game(score, result["game_id"], self.id, round_number)
    
    def actualise_players_score(self, round_number):
        """actualise players score after each round"""
        with open('data/tournaments.json') as file:
            data = json.load(file)

        for tournament in data['tournaments']:
            if tournament['id'] == self.id:
                target_tournament = tournament
                break

        round = target_tournament['rounds'][round_number]
        for game in round["games"]:
            player1 = game[0]["player1"]
            player2 = game[1]["player2"]

            score1 = game[0]["score"]
            score2 = game[1]["score"]

            for player in target_tournament["players"]:
                if player["id"] == player1["id"]:
                    player["score"] = player.get("score", 0) + score1
                elif player["id"] == player2["id"]:
                    player["score"] = player.get("score", 0) + score2
            
            for player in self.players:
                if player["id"] == player1["id"]:
                    player["score"] = player.get("score", 0) + score1
                elif player["id"] == player2["id"]:
                    player["score"] = player.get("score", 0) + score2
        
        with open("data/tournaments.json", "w") as json_file:
            json.dump(data, json_file)

    def check_if_game_already_occurred(self, player1, player2):
        """check if a confrontation between two players already occured"""
        for round in self.rounds:
            for game in round.games:
                is_player_a_match = game.player_a["id"] == player1["id"] or game.player_a["id"] == player2["id"]
                is_player_b_match = game.player_b["id"] == player1["id"] or game.player_b["id"] == player2["id"]
                if is_player_a_match and is_player_b_match:
                    print("TEST - La confrontation a déja eu lieu")
                    return True
                else:
                    return False

    def pair_players(self):
        """return list of games"""
        games = []
        if len(self.rounds) == 1:
            self.shuffle_players()
            for i in range(0, len(self.players), 2):
                player1 = self.players[i]
                player2 = self.players[i + 1]
                games.append(Game(player1, player2))
        
        else:
            sorted_players = sorted(self.players, key=lambda player: player["score"], reverse=True)
            player_index = 1
            while len(sorted_players) > 0:
                player1 = sorted_players[0]
                player2 = sorted_players[player_index]
                if not self.check_if_game_already_occurred(player1, player2):
                    games.append(Game(player1, player2))
                    del sorted_players[player_index]
                    del sorted_players[0]
                    player_index = 1
                
                else:
                    player_index = player_index + 1
                    if player_index == len(sorted_players) - 1:
                        player1 = self.players[0]
                        player2 = self.players[player_index]
                        games.append(Game(player1, player2))
                        del sorted_players[player_index]
                        del sorted_players[0]
        return games
    
    def shuffle_players(self):
        """shuffle player randomly"""
        random.shuffle(self.players)
     
    def get_and_save_winners(self):
        """return tournament winner/s """
        sorted_players = sorted(self.players, key=lambda player: player["score"], reverse=True)
        winners = [player for player in self.players if player['score'] == sorted_players[0]['score']]

        with open('data/tournaments.json', 'r') as file:
            data = json.load(file)
        for tournament in data['tournaments']:

            if tournament['id'] == self.id:
                tournament['winners'] = winners
                break

        with open('data/tournaments.json', 'w') as file:
            json.dump(data, file, indent=4)

        return winners
    
    def close_tournament(self):
        self.end_date = datetime.now()
        with open('data/tournaments.json', 'r') as file:
            data = json.load(file)
        for tournament in data['tournaments']:

            if tournament['id'] == self.id:
                tournament['end_date'] = self.end_date.strftime("%Y-%m-%d %H:%M"),
                break

        with open('data/tournaments.json', 'w') as file:
            json.dump(data, file, indent=4)
