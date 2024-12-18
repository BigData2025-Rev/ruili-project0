from GameLogic.Game import Game
from GameLogic.GamePad import GamePad
from GameLogic.Snake import Snake
from GameLogic.Fruit import Fruit

def gameStart():
    print("Hello! Game Start!")
    game = Game()
    userInput = "Y"
    
    while(userInput != "N"):
        print("Round Start!")
        game.run()
        print("Round End!")
        userInput = input("Do you want to start a nwe Round? [Y/N] ")
        while(userInput not in "YN"):
            userInput = input("Do you want to start a nwe Round? [Y/N] ")
    print("Game End!")

gameStart()