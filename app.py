#Python Web Development Techdegree
#Project 2 - Basketball Team Stat Tool

import constants
import random
from copy import deepcopy
import os



teams = deepcopy(constants.TEAMS)
players = deepcopy(constants.PLAYERS)


#Welcome page with select for stats

print("BASKETBALL TEAM STATS TOOL\n")
    while True:
        print("----MENU----\n1) Display Team Stats\n2)QUIT\n")
        menu_input = input("Enter an option >  ")
        while menu_input != "1" and menu_input != "2":
            clear_screen()
            menu_input = input("The is not a valid selection\nPlease enter either 1 for TEAM STATS or 2 to QUIT the program\n\n-----------MENU-----------\n\n1) Display Team Stats\n2)QUIT\n>  ")

        if menu_input == "1":
            team_menu()
        else:
            clear_screen()
            print("Good Bye")
            break

#add players
def playerAdd():

    players
    numberOfPlayers = 0
    teams = []
    nums = set()

    while len(num) < 6:
        nums.add(random.choice(players))

    for num in nums:
        team.append(players[num]["name"])
        numberOfPlayers += 1
        all.remove(num)

    return num_players, team


