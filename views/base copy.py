import datetime


class View:

    def intro_message(self):
        print("Hello, Welcome to our tournament")

    def get_tournament_name(self):
        self.name = input("How would you like to call your tournament ?")
        print(self.name + "? That's an excellent name")
        return self.name
    
    def get_tournament_location(self):
        self.location = input("Where will the torunament be held ?")
        print("Nice ! ")
        return self.location
    
    def get_tournament_start_date(self):
        self.start_date = datetime.datetime.strptime(input("When does it start ? (in DD/MM/YYYY)"),"%d/%m/%Y").date()
        return self.start_date
    
    def get_tournament_end_date(self):
        while True: 
            self.end_date = datetime.datetime.strptime(input("And when does it finish (in DD/MM/YYYY)? "),"%d/%m/%Y").date()
            if (self.end_date >= self.start_date):
                print("perfect !")
                return self.start_date
            else:
                print("The end date has to be after the start date !")

    def get_players(self, players_ids):
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
            players.append(("YR27653", "YR34681", "DT91027", "TF52376", "CT83941", "KX57234", "LE65874", "ZD22348"))
        else:
            print("Réponse invalide.")
        
        return players
        

    
