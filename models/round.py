class Round:
    def __init__(self, name, start_date, closed=False, end_date=None):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.games = []
        self.closed = closed

    def add_games(self, games):
        self.games = games
    
    def close_game(self, player1, score1, player2, score2):
        game = ([player1, score1], [player2, score2])
        self.games.append(game)

    def close_round(self, end_date):
        self.end_date = end_date  #ou self.end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") ? 