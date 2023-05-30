import datetime


class View:

    @staticmethod
    def intro_message():
        print("Hello, Welcome to our tournament")
        print("Nombre de joeur pair requis...")#####
    
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
        while True:
            try: 
                start_date = datetime.datetime.strptime(input("When does it start ? (in DD/MM/YYYY)"),"%d/%m/%Y").date()
                return start_date
            except ValueError:
                print("Invalid answer")
                continue
        
    
    @staticmethod
    def get_tournament_end_date(start_date):
        while True:
            try:
                end_date = datetime.datetime.strptime(input("And when does it finish (in DD/MM/YYYY)? "),"%d/%m/%Y").date()
                if (end_date >= start_date):
                    print("perfect !")
                    return start_date
                else:
                    print("The end date has to be after the start date !")
            except ValueError:
                print("Invalid answer")
                continue

    @staticmethod
    def get_players(players_ids):
        "register player to tournament"
        print("It's now time to register players")
        while True:
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
                print("Invalid answer")
                continue
            
            return players

    @staticmethod
    def start_tournament_or_register_player():
        while True:
            response = input("Do you want to start a tournament (1) or register players (2)") 
            if response not in ["1", "2"]:
                print("Invalid answer")
                continue
            return response 
    
    @staticmethod
    def register_player():
        "register_player_to_the_federation"
        first_name = input("enter first name :") 
        last_name = input("enter last name :")
        id = input("enter id :")
        date_of_birth = input("enter date of birth ")
        return {"first_name": first_name, "last_name": last_name, "id": id, "date_of_birth": date_of_birth}

    @staticmethod
    def show_games(games, round_number):
        print(f"Hello, here are the games for round n{round_number} :")
        print("One you have entered all the scores next round will be launched : ")
        i = 0
        for game in games:
            print(f"ID {i} :  {game.player_a['first_name']} {game.player_a['last_name']} VS {game.player_b['first_name']} {game.player_b['last_name']}")
            i = i + 1

    @staticmethod
    def input_result(games):
        while True:
            result_input = input("Choisissez un jeu (entrez l'ID du jeu). Si vous souhaitez clôturer la manche, saisissez 'closed' (tous les scores doivent être ajoutés avant) : ")
            
            if result_input == "closed":
                return "closed"
    
            try: 
                if int(result_input) in list(range(len(games))):
                    game_id = int(result_input)
                    game = games[game_id]
                    print(f"ID {game_id}: {game.player_a['first_name']} {game.player_a['last_name']} VS {game.player_b['first_name']} {game.player_b['last_name']}")
                    winner = input("Maintenant, saisissez le gagnant : A, B ou D pour un match nul : ")
                    if winner not in ["A", "B", "D"]:
                        print("Entrée invalides, vous devez saisir A,B ou D")
                        continue
                    return {"winner": winner, "game_id": game_id}
        
                else:
                    print("Entrée invalide. Veuillez saisir 'closed' pour clôturer la manche ou un nombre valide.")
                    continue
            except:
                print("Entrée invalide. Veuillez saisir 'closed' pour clôturer la manche ou un nombre valide.")
                continue
    
    @staticmethod
    def close_tournament(tournament_winners):
        print('Thanks, the tournament is over')

        if len(tournament_winners) == 1:
            winner = tournament_winners[0]
            print(f"Congratulation to {winner['first_name']} {winner['last_name']} who won the tournament with a score of {winner['score']}")
        else:
            print("Congratulation to")
            for player in tournament_winners:
                print(f"{player['first_name']} {player['last_name']},")
            print(f"who won the tournament with a score of {player['score']}")
    
    @staticmethod
    def id_already_existing(id):
        print(f"L'id {id} existe déjà.")

    @staticmethod
    def register_player_to_fd_success_message(first_name):
        print(f"Le joueur {first_name} a été ajouté avec succès.")

    @staticmethod
    def no_player_found(id):
        print(f"Aucun joueur avec l'ID {id} n'a été trouvé.")


       

