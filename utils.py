
import subprocess
import os
import sys
# from views.views import View 

def go_back_to_menu_or_exit_programme(user_input):
    if user_input.lower() == "menu":
        os.system('cls' if os.name == 'nt' else 'clear') 
        subprocess.call(["python", "main.py"])

    if user_input.lower() == "exit":
        os.system('cls' if os.name == 'nt' else 'clear')
        # View.goodbye()
        sys.exit()