import random
import numpy as np

class Fruit:
    def __init__(self):
        self.position = None
        self.fruitScore = 1
    
    def update(self, gameMap):
        mapWidth = len(gameMap[0])
        mapHeight = len(gameMap)

        if self.position is None:
            # this is the init of the fruit
            self.position = [0, 0]
        else:
            # this is update, check if snake ate the fruit
            # generate a new fruit if snake ate fruit
            # and return the score earned
            pass
        
        return 0
    
    def getPosition(self):
        return self.position