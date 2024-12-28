import os
from .ANSI import ANSI

class GamePad:
    def __init__(self):
        self.wallHit = False
        self.mapHeight = 0
        self.mapWidth = 0
        self.map = []

    def initGameMap(self):
        # ask user for game map chose
        userInput = self.askUserMapChoice()
        mapFilePath = os.path.join(os.path.dirname(__file__), '../Resources/GameMap' + userInput + '.txt')
        with open(mapFilePath, "r", encoding="utf-8") as mapFile:
            content = mapFile.read()
            lines = content.split("\n")
            self.mapHeight = len(lines)
            self.mapWidth = len(lines[0])
            # Store the mao in a 2d array
            self.map = [list(line) for line in lines]

    # render the map, including the snake and the fruit
    def paint(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # 清屏

        for row in self.map:
            styled_row = []
            for char in row:
                if char == "*":  # wall, bold red
                    styled_row.append(f"{ANSI.BOLD}{ANSI.RED}{char}{ANSI.RESET}")
                elif char == "F":  # fruit, yellow
                    styled_row.append(f"{ANSI.BOLD}{ANSI.YELLOW}{char}{ANSI.RESET}")
                elif char in "sH":  # snake, blue
                    styled_row.append(f"{ANSI.BOLD}{ANSI.CYAN}{char}{ANSI.RESET}")
                else: 
                    styled_row.append(char)
            print(" ".join(styled_row))

    # update the position of the snake
    def updateSnake(self, snakePosition):
        # clear the old snake and the fruit first
        for row in range(self.mapHeight):
            for col in range(self.mapWidth):
                if self.map[row][col] in "sHF":
                    self.map[row][col] = " "

        # add the new position of the snake
        for position in snakePosition:
            if self.map[position[0]][position[1]] == "*":
                self.wallHit = True
            self.map[position[0]][position[1]] = "s"
        # The head should be "H"
        self.map[snakePosition[-1][0]][snakePosition[-1][1]] = "H"
    # add the position of the fruit
    def updateFruit(self, fruitPosition):
        self.map[fruitPosition[0]][fruitPosition[1]] = "F"

    def getGameMap(self):
        return self.map

    def isSnakeHitWall(self):
        return self.wallHit
    
    def askUserMapChoice(self):
        
        print(f"{ANSI.BOLD}\nPlease pick which map you want to play: {ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[1]{ANSI.RESET}I want to play EASY.{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[2]{ANSI.RESET}I want to play MEDIUM.{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.YELLOW}[3]{ANSI.RESET}I want to play HARD.{ANSI.RESET}")
        userInput = input(f"{ANSI.BOLD}{ANSI.YELLOW}Please enter 1 ~ 3: {ANSI.RESET}")
        
        while not userInput in "123":
            print("Your input must be 1 or 2 or 3")
            userInput = input(f"{ANSI.BOLD}{ANSI.YELLOW}Please enter 1 ~ 3: {ANSI.RESET}")
        return userInput