import os
from GameLogic.Game import Game
from GameLogic.UserAccount import UserAccount
from GameLogic.ANSI import ANSI

def gameStart():
    print("<---------- SNAKE GAME ---------->")
    
    while(True):
        userInput = showInstruction()
        if userInput == '1':
            UserAccount.showScoreRankBoard()
        elif userInput == '2':
            game = Game()
            game.run()
        elif userInput == '3':
            break
        else:
            print("Oops, something wrong here, I accepted an wrong input.")
    
    print("\nGame End!")

def showInstruction():

    # check if user logged in first
    while not UserAccount.isLoggedIn():
        print(f"{ANSI.BOLD}You have not logged in yet.{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[1]{ANSI.RESET}{ANSI.BOLD}I want to log in.{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[2]{ANSI.RESET}{ANSI.BOLD}I want to register.{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[3]{ANSI.RESET}{ANSI.BOLD}I want to quit.{ANSI.RESET}")
        userInput = input(f"{ANSI.BOLD}{ANSI.YELLOW}Please enter 1 ~ 3: {ANSI.RESET}")
        if userInput == "1": UserAccount.login()
        elif userInput == "2": UserAccount.register()
        elif userInput == "3": return 3


    print("""Instruction:
[1] Check the historical score rank
[2] Start a new round
[3] End game""")
    userInput = input("Please enter 1 ~ 3: ")
    while(len(userInput) == 0 or not userInput in "123"):
        userInput = input("Please enter 1 ~ 3: ")
    return userInput

gameStart()