import constants


#Welcome page with select for stats

def welcomeMenu():
    print('''
    Welcome to the this seasons stat sheet!
    Please select a choice to continue or quit
    1. Display Stats
    2. Quit
    ''')


    choice = print("Please select an option: ")
    choice = int(choice)

    while choice == 1:
