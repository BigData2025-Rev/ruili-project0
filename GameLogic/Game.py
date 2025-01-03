from .Snake import Snake
from .GamePad import GamePad
from .Fruit import Fruit
from .UserAccount import UserAccount
from .ANSI import ANSI
import keyboard
import time
import msvcrt

class Game:
    def __init__(self):
        self.gamePad = GamePad()
        self.snake = Snake()
        self.fruit = Fruit()

        self.userInput = ""
        self.score = 0
        self.gameEnd = False
    
    def run(self):
        # init the gameMap, snake position and generate a fruit
        self.gamePad.initGameMap()
        self.snake.initPosition(self.gamePad.getGameMap())
        self.fruit.update(self.gamePad.getGameMap(), self.snake.getPosition())
        self.gamePad.updateSnake(self.snake.getPosition())
        self.gamePad.updateFruit(self.fruit.getPosition())
        print(f"\n{ANSI.RED}{ANSI.BOLD}New Round Start In 3 Seconds!{ANSI.RESET}")
        print(f"{ANSI.ITALIC}{ANSI.BOLD}Press W-A-S-D to move the snake and eat the fruit!{ANSI.RESET}")
        time.sleep(3)
        
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
            print(f"{ANSI.BOLD}{ANSI.ITALIC}You hit the wall!{ANSI.RESET}")
        else:
            print(f"{ANSI.BOLD}{ANSI.ITALIC}You ate yourself!{ANSI.RESET}")
        UserAccount.addScore(self.score)
        print(f"{ANSI.BOLD}{ANSI.ITALIC}Your final score is {ANSI.RED}{self.score}{ANSI.RESET}")
        print(f"{ANSI.RED}{ANSI.BOLD}Round End!{ANSI.RESET}\n")

        self.clear_input_buffer()

    def setUserInput(self):
        self.userInput = keyboard.read_event().name
        time.sleep(0.1)

    def clear_input_buffer(self):
        while msvcrt.kbhit():
            msvcrt.getch()
