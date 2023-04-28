class Game:
    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b
    
    def attribute_score(self, result):
        if result == "player A":
            self.score_a = 1
            self.score_b = 0
        
        elif result == "player B":
            self.score_a = 0
            self.score_b = 1

        if result == "draw":
            self.score_a = 0.5
            self.score_b = 0.5



        
