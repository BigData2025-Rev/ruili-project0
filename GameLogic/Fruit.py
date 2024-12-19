import random
import numpy as np

class Fruit:
    def __init__(self):
        self.position = None
        self.fruitScore = 1
    
    def genera(self, gameMap):
        mapWidth = gameMap.shape[1]
        mapHeight = gameMap.shape[0]

        if self.position is None:
            # this is the init of the fruit
            self.position = [0, 0]
        else:
            # this is update, check if snake ate the fruit
            # generate a new fruit if snake ate fruit
            # and return the score earned
            pass
    
    def getPosition(self):
        return self.position