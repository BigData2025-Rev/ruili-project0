import os
from GameLogic.Game import Game
from GameLogic.ScoreRank import ScoreRank

def gameStart():
    while(True):
        userInput = showInstruction()
        if userInput == '1':
            print(ScoreRank.readScoreRank())
        elif userInput == '2':
            game = Game()
            game.run()
        else:
            print("Oops, something wrong here, I accepted an wrong input.")
    
    print("\nGame End!")

def showInstruction():
    print("<---------- SNAKE GAME ---------->")
    print("Instruction: ")
    print("""
        [1] Check the historical score rank
        [2] Start a new round
          """)
    userInput = input("Please enter 1 or 2: ")
    while(not userInput in "12"):
        userInput = input("Please enter 1 or 2: ")
    return userInput

gameStart()