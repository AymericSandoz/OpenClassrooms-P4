import datetime


class View:

    @staticmethod
    def intro_message():
        print("Hello, Welcome to our tournament")
    
    @staticmethod
    def invalid_answer():
        print("Invalid answer")

    @staticmethod
    def get_tournament_name():
        name = input("How would you like to call your tournament ?")
        print(name + "? That's an excellent name")
        return name
    
    @staticmethod
    def get_tournament_location():
        location = input("Where will the torunament be held ?")
        print("Nice ! ")
        return location
    
    @staticmethod
    def get_tournament_start_date():
        start_date = datetime.datetime.strptime(input("When does it start ? (in DD/MM/YYYY)"),"%d/%m/%Y").date()
        return start_date
    
    @staticmethod
    def get_tournament_end_date(start_date):
        while True: 
            end_date = datetime.datetime.strptime(input("And when does it finish (in DD/MM/YYYY)? "),"%d/%m/%Y").date()
            if (end_date >= start_date):
                print("perfect !")
                return start_date
            else:
                print("The end date has to be after the start date !")

    @staticmethod
    def get_players(players_ids):
        "register player to tournament"
        print("It's now time to register players")
        reponse = input("Do you want to add manually players (1) or choose a list of preregistrered players (2)")  
        players = []
        if reponse == "1":
            while True:
                id = input("Please enter player's id. (or enter 'q' to stop) : ")
                if id == "q":
                    break
                elif id in players:
                    print(f"{id} has already been added.")
                elif id not in players_ids:
                    print(f"{id} not registered in our list of player.")
                else:
                    players.append((id))
        elif reponse == "2":
            players.extend(["YR27653", "YR34681", "DT91027", "TF52376", "CT83941", "KX57234", "LE65874", "ZD22348"])#permet d'ajouter les éléments directement dans la liste [] au lieu de les impriquer
        else:
            print("Réponse invalide.")
        
        return players

    @staticmethod
    def start_tournament_or_register_player():
        response = input("Do you want to start a tournament (1) or register players (2)") 
        return response 
    
    @staticmethod
    def register_player():
        "register_player_to_the_federation"
        first_name = input("enter first name :") 
        last_name = input("enter last name :")
        id = input("enter id :")
        date_of_birth = input("enter date of birth ")
        return {"first_name": first_name, "last_name": last_name, "id":id, "date_of_birth": date_of_birth}

    @staticmethod
    def show_games(games, round_number):
        print(f"Hello, here are the games for round n{round_number} :")
        print("One you have entered all the scores next round will be launched :")
        i = 0
        for game in games:
            print(f"ID {i} :  {game.player_a['first_name']} {game.player_a['last_name']} VS {game.player_b['first_name']} {game.player_b['last_name']}")
            i = i + 1

    @staticmethod
    def input_result(games):
        result_input = input("now choose a game (enter the id of the game) \nAlso if you want to close the round enter close (all score must be added before):")
        if result_input == "closed":
            return "closed"
        
        game_id = int(result_input)  
        game = games[game_id]
        print(f"ID {game_id} :  {game.player_a['first_name']} {game.player_a['last_name']} VS {game.player_b['first_name']} {game.player_b['last_name']}")
        winner = input(f"now enter the winner : A, B or D as draw")
        return {"winner" : winner, "game_id" : game_id}

       

