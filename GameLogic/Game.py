from .Snake import Snake
from .GamePad import GamePad
from .Fruit import Fruit
from .ScoreRank import ScoreRank
import numpy as np

class Game:
    def __init__(self):
        self.gamePad = GamePad()
        self.snake = Snake()
        self.fruit = Fruit()

        self.userInput = ""
        self.score = 0
        self.gameEnd = False
    
    def run(self):
        print("\nRound Start!")
        print("Press W-A-S-D to move the snake and eat the fruit!")
        # init the gameMap, snake position and generate a fruit
        self.gamePad.initGameMap()
        self.snake.initPosition(self.gamePad.getGameMap())
        self.fruit.update(self.gamePad.getGameMap(), self.snake.getPosition())
        self.gamePad.updateSnake(self.snake.getPosition())
        self.gamePad.updateFruit(self.fruit.getPosition())

        while not self.gameEnd:
            
            self.gamePad.paint()

            self.setUserInput()
            
            self.snake.move(self.userInput, self.fruit.getPosition())
            self.score += self.fruit.update(self.gamePad.getGameMap(), self.snake.getPosition())
            self.gamePad.updateSnake(self.snake.getPosition())
            self.gamePad.updateFruit(self.fruit.getPosition())

            self.gameEnd = self.gamePad.isSnakeHitWall() or self.snake.isSnakeHitItself()

        self.gamePad.paint()
        if(self.gamePad.isSnakeHitWall()):
            print("You hit the wall!")
        else:
            print("You ate yourself!")
        ScoreRank.addScore(self.score)
        print("Your final score is " + str(self.score))
        print("Round End!\n")

    def setUserInput(self):
        self.userInput = input()
