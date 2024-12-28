import os
from GameLogic.Game import Game
from GameLogic.UserAccount import UserAccount
from GameLogic.ANSI import ANSI

def gameStart():
    print(f"{ANSI.BOLD}{ANSI.CYAN}<------------------------- SNAKE GAME ------------------------->{ANSI.RESET}")
    GameLoop()
    print("\nGame End!")

def GameLoop():
    # check if user logged in first
    while not UserAccount.isLoggedIn():
        print(f"{ANSI.BOLD}{ANSI.RED}You have not logged in yet.{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[1]{ANSI.RESET}I want to log in.{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[2]{ANSI.RESET}I want to register.{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[3]{ANSI.RESET}I want to quit.{ANSI.RESET}")
        userInput = input(f"{ANSI.BOLD}{ANSI.YELLOW}Please enter 1 ~ 3: {ANSI.RESET}")
        if userInput == "1": UserAccount.login()
        elif userInput == "2": UserAccount.register()
        elif userInput == "3": return 3
        else: print(f"{ANSI.BOLD}{ANSI.RED}Please enter number between 1~3\n{ANSI.RESET}")

    while True:
        print(f"{ANSI.BOLD}{ANSI.GREEN}\nWelcome, {UserAccount.currentAccount}{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[1]{ANSI.RESET}I want to check the historical score rank.{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[2]{ANSI.RESET}I want to start a new round.{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[3]{ANSI.RESET}I want to quit.{ANSI.RESET}")
        userInput = input(f"{ANSI.BOLD}{ANSI.YELLOW}Please enter 1 ~ 3: {ANSI.RESET}")
        if userInput == "1": UserAccount.showScoreRankBoard()
        elif userInput == "2": game = Game(); game.run()
        elif userInput == "3": return
        else: print(f"{ANSI.BOLD}{ANSI.RED}Please enter number between 1~3\n{ANSI.RESET}")

gameStart()