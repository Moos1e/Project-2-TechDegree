import constants
from copy import deepcopy
import os



players = constants.PLAYERS
teams = constants.TEAMS
#Welcome page with select for stats

def welcomeMenu():
    print('''
    Welcome to the this seasons stat sheet!
    Please select a choice to continue or quit
    1. Display Stats
    2. Quit
    ''')

def option():
    selection = input("Please select an option")

    while selection:
        selection = int(selection)
        if selection == '1'

        try:
            selection = int(selection)
            if selection != 1 and selection != 2:
                raise ValueError("Please type in a number that is 1 or 2")
        continue
    else:
        return selection

#Teams
def teams():
    panthers = []
    warriors = []
    bandits = []