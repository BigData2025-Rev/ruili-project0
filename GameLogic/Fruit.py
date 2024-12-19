import random
import numpy as np

class Fruit:
    def __init__(self):
        self.position = None
        self.fruitScore = 1
    
    def update(self, gameMap, snakePosition):
        
        if self.position is None:
            newPosition = self.generateNewPosition(gameMap)
            self.position = [newPosition[0], newPosition[1]]
            return 0
        else:
            # this is update, check if snake ate the fruit
            # generate a new fruit if snake ate fruit
            # and return the score earned
            if(self.position in snakePosition):
                newPosition = self.generateNewPosition(gameMap)
                self.position = [newPosition[0], newPosition[1]]
                return self.fruitScore
            else:
                return 0
    
    def generateNewPosition(self, gameMap):
        mapWidth = len(gameMap)
        mapHeight = len(gameMap[0])

        initX = random.randint(1, mapWidth) - 1
        initY = random.randint(1, mapHeight) - 1
            
        while gameMap[initX][initY] != " ":
            initX = random.randint(1, mapWidth) - 1
            initY = random.randint(1, mapHeight) - 1
        
        return [initX, initY]

    def getPosition(self):
        return self.position