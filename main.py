import os
from GameLogic.Game import Game
from GameLogic.ScoreRank import ScoreRank

def gameStart():
    print("<---------- SNAKE GAME ---------->")
    
    while(True):
        userInput = showInstruction()
        if userInput == '1':
            ScoreRank.showScoreRankBoard()
        elif userInput == '2':
            game = Game()
            game.run()
        elif userInput == '3':
            break
        else:
            print("Oops, something wrong here, I accepted an wrong input.")
    
    print("\nGame End!")

def showInstruction():
    print("""Instruction:
        [1] Check the historical score rank
        [2] Start a new round
        [3] End game""")
    userInput = input("Please enter 1 ~ 3: ")
    while(not userInput in "123"):
        userInput = input("Please enter 1 ~ 3: ")
    return userInput

gameStart()