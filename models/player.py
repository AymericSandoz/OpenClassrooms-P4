import json


class Player:
    def __init__(self, first_name, last_name, id, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.date_of_birth = date_of_birth
        self.score = None

    def register_player(self):
        """register to the Federation"""
        with open("data/players.json", 'r') as f:
            players = json.load(f)["players"]
            ids = [p["id"] for p in players]
            if self.id in ids:
                return "error"
        players.append(vars(self))

        with open("data/players.json", 'w') as f:
            jsonObject = {"players": players}
            json.dump(jsonObject, f)
            return "success"
