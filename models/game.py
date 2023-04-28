class Game:
    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b
    
    @staticmethod
    def attribute_score(result):
        print("result : ", result)
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
        print("score :", score)
        return score



        
