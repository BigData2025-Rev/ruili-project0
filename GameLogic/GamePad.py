import os
import numpy as np

class GamePad:
    def __init__(self):
        
        self.wallHit = False
        self.mapHeight = 0
        self.mapWidth = 0
        self.map = np.empty((0, 0), dtype=str)


    def initGameMap(self):
        # Get game map from file
        # store map in an np array
        mapFilePath = os.path.join(os.path.dirname(__file__), '../Resources/GameMap2.txt')
        with open(mapFilePath, "r", encoding="utf-8") as mapFile:
            content = mapFile.read()
            lines = content.split("\n")
            self.mapHeight = len(lines)
            self.mapWidth = len(lines[0])
            self.map = np.empty((self.mapHeight, self.mapWidth), dtype=str)
            
            for row in range(self.mapHeight):
                for column in range(self.mapWidth):
                    self.map[row][column] = lines[row][column]

    # paint the gamepad, including map, snake, fruit
    def paint(self):
        for row in self.map:
            for char in row:
                print(char, end="")
            print()

    # update the game map, include the snake and fruit
    def update(self, snakePosition, fruitPosition):
        for position in snakePosition:
            if(self.map[position[0]][position[1]] == "*"):
                self.wallHit = True
            self.map[position[0]][position[1]] = "s"
        
        self.map[fruitPosition[0]][fruitPosition[1]] = "x"

    def getGameMap(self):
        return self.map

    def isSnakeHitWall(self):
        return self.wallHit
                 


    