from .Snake import Snake
from .GamePad import GamePad
from .Fruit import Fruit

class Game:
    def __init__(self):
        self.gamePad = GamePad()
        self.snake = Snake()
        self.fruit = Fruit()

        self.userInput = ""
        self.score = 0
        self.gameEnd = False
    
    def run(self):
        
        while not self.gameEnd:
            
            self.gamePad.paint([], [])

            self.setUserInput()
            print("You entered: " + self.userInput)
            if self.userInput == "end":
                self.gameEnd = True
            
            self.snake.move(self.userInput)
            self.score += self.fruit.update(self.snake)
            self.gamePad.update(self.snake.getPosition(), self.fruit.getPosition())

            self.gameEnd = self.gamePad.isSnakeHitWall() and self.snake.isSnakeHitItself()

    def setUserInput(self):
        self.userInput = input()
