import json
from datetime import datetime

class Round:
    def __init__(self, name, closed=False):
        self.name = name
        self.start_date = datetime.now()
        self.games = []
        self.closed = closed

    def add_games(self, games, tournamentId, round_number):
        self.games = games
        with open('data/tournaments.json') as file:
            data = json.load(file)

        tournament = next((t for t in data['tournaments'] if t['id'] == tournamentId), None)#pas compris pourquoi, #chatgpt //  rechercher un tournoi spécifique dans la liste  data['tournaments'].
        #next() est une fonction qui retourne le prochain élément d'un itérable qui répond à une condition donnée. Dans ce cas, il retourne le premier tournoi qui correspond à la condition t['id'] == tournamentId.
        if tournament:
            if round_number == 1:
                tournament['rounds'] = [{"start_date" : self.start_date.strftime("%Y-%m-%d %H:%M"), "games" : [game.to_dict() for game in games], "round_number" : round_number, "closed" : False}]
            else:
                tournament['rounds'].append({"start_date" : self.start_date.strftime("%Y-%m-%d %H:%M"), "games" : [game.to_dict() for game in games], "round_number" : round_number, "closed" : False})
            for t in data['tournaments']:
                if t['id'] == tournamentId:
                    t = tournament
                    break
            with open('data/tournaments.json', 'w') as file:
                json.dump(data, file, indent=4)

    def close_round(self, tournamentId, round_number):
        self.end_date = datetime.now()
        self.closed = True
        with open('data/tournaments.json') as file:
            data = json.load(file)

        for tournament in data['tournaments']:
            if tournament['id'] == tournamentId:
                target_tournament = tournament
                break

        rounds = target_tournament['rounds']
        games = rounds[round_number]['games']
        for game in games:
            for player in game:
                if player['score'] is None:
                    self.closed = False
                    break
        if self.closed is True:
            rounds[round_number-1]["closed"] = True
            rounds[round_number-1]["end_date"] = self.end_date.strftime("%Y-%m-%d %H:%M")
            with open("data/tournaments.json", "w") as json_file:
                json.dump(data, json_file)


 



