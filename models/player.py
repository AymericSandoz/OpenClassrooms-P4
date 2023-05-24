import json
from views.views import View


class Player:
    def __init__(self, first_name, last_name, id, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.date_of_birth = date_of_birth
        self.score = None
    
    def register_player(self): #note : pour cette fonction il faudrait vérifier que l'id rentré correspond au format désiré : 11XXXXX
        """register to the Federation"""
        with open("data/players.json", 'r') as f:
            players = json.load(f)["players"] #prend un fichier jsone t créer une version python de l'objet
            ids = [p["id"] for p in players]
            if self.id in ids:
                View.id_already_existing(self.id)
                return
            
        players.append(vars(self))

        with open("data/players.json", 'w') as f:
            jsonObject = {"players": players}
            json.dump(jsonObject, f) #prend un fichier python et créer une version json de cet objet 
            View.register_player_to_fd_success_message(self.first_name)
    
    def get_player_info(self, player_id):
        """Get player's info by ID"""
        with open("data/players.json", 'r') as f:
            players = json.load(f)["players"]
            for player in players:
                if player["id"] == player_id:
                    return player
            View.no_player_found(player_id)
            return None