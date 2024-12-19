import os

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
        for row in self.map:
            print("".join(row)

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
        askInstruction = """Please pick which map you want to play:\n[1] Easy\n[2] Medium\n[3] Hard\nEnter 1 or 2 or 3: """
        userMapChoice = input(askInstruction)
        while not userMapChoice in "123":
            print("Your input must be 1 or 2 or 3")
            userMapChoice = input(askInstruction)
        return userMapChoice