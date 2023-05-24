import json

class Game:
    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.score_a = None
        self.player_b = player_b
        self.score_b = None
    
    @staticmethod
    def attribute_score(result):
        if result == "A":
            score_a = 1
            score_b = 0
        
        elif result == "B":
            score_a = 0
            score_b = 1

        elif result == "D":
            score_a = 0.5
            score_b = 0.5
        
        else:
            return "error : wrong result. Must be A, B or D"
        
        score = {"score_a": score_a, "score_b": score_b}
        return score
    
    @staticmethod
    def close_game(score, gameId, tournamentId, round_number):
        with open('data/tournaments.json') as file:
            data = json.load(file)

        for tournament in data['tournaments']:
            if tournament['id'] == tournamentId:
                target_tournament = tournament
                break

        rounds = target_tournament['rounds'][round_number]

        game = rounds['games'][gameId]

        player1 = game[0]['player1']
        player2 = game[1]['player2']

        rounds['games'][gameId] = [{'player1': player1, 'score': score["score_a"]}, {'player2': player2, 'score': score["score_b"]}]

        with open('data/tournaments.json', 'w') as file:
            json.dump(data, file, indent=4)

    
    def to_dict(self):
        return [{'player1': self.player_a, 'score': None}, {'player2': self.player_b, 'score': None}]



        
