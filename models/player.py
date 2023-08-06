import json
import random
import string


class Player:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.id = self.generate_player_id()
        self.date_of_birth = date_of_birth.strftime("%m/%d/%Y")

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

    @staticmethod
    def generate_player_id():
        """generate an id with the format XX12345"""
        # Generate two capital letters
        letters = random.choices(string.ascii_uppercase, k=2)
        # Generate 5 digits
        digits = random.choices(string.digits, k=5)
        id = ''.join(letters) + ''.join(digits)
        return id
