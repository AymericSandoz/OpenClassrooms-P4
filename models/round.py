import json


class Round:
    def __init__(self, name, start_date, closed=False, end_date=None):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.games = []
        self.closed = closed

    def add_games(self, games, tournamentId):
        print("games",games)
        self.games =  games
        with open('data/tournaments.json') as file:
            data = json.load(file)

        tournament = next((t for t in data['tournaments'] if t['id'] == tournamentId), None)
        if tournament:
            tournament['games'] = [game.to_dict() for game in games]
            for t in data['tournaments']:
                if t['id'] == tournamentId:
                    t = tournament
                    break
            with open('data/tournaments.json', 'w') as file:
                json.dump(data, file, indent=4)

    def close_round(self, tournamentId):
        self.end_date = "23/10/1996"  #ou self.end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") ? 
        self.closed = True
        with open('data/tournaments.json') as file:
            data = json.load(file)

        for tournament in data['tournaments']:
            if tournament['id'] == tournamentId:
                target_tournament = tournament
                break

        games = target_tournament['games']
        for game in games:
            for player in game:
                if player['score'] is None:
                    self.closed = False
                    break


