import json


class Player:
    def __init__(self, first_name, last_name, id, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.date_of_birth = date_of_birth
    
    def register_player(self): #note : pour cette fonction il faudrait vérifier que l'id rentré correspond au format désiré : 11XXXXX
        """register to the Federation"""
        with open("data/players.json", 'r') as f:
            players = json.load(f)["players"] #prend un fichier jsone t créer une version python de l'objet
            ids = [p["id"] for p in players]
            if self.id in ids:
                print(f"L'id {self.id} existe déjà.")
                return
            
        players.append(vars(self))
        print(players)

        with open("data/players.json", 'w') as f:
            jsonObject = {"players": players}
            print(jsonObject)
            json.dump(jsonObject, f) #prend un fichier python et créer une version json de cet objet 
            print(f"Le joueur {self.first_name} a été ajouté avec succès.")
    
    def get_player_info(self, player_id):
        """Get player's info by ID"""
        with open("data/players.json", 'r') as f:
            players = json.load(f)["players"]
            for player in players:
                if player["id"] == player_id:
                    return player
            print(f"Aucun joueur avec l'ID {player_id} n'a été trouvé.")
            return None