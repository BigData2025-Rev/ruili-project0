import numpy as np

class Snake:
    def __init__(self):
        self.position = []
        self.hitMyself = False
    
    def initPosition(self, gameMap):
        initX = gameMap.shape[1]//2
        initY = gameMap.shape[0]//2
        if gameMap[initX][initY] != " ":
            initX -= 1
        self.position.append([initX, initY])

    def getPosition(self):
        return self.position
    
    def move(self, direction, fruitPosition):
        direction = direction.upper()
        if direction == "W":
            newPosition = [self.position[-1][0], self.position[-1][1]+1]
        elif direction == "A":
            newPosition = [self.position[-1][0]-1, self.position[-1][1]]
        elif direction == "S":
            newPosition = [self.position[-1][0], self.position[-1][1]-1]
        elif direction == "D":
            newPosition = [self.position[-1][0]+1, self.position[-1][1]]
        else:
            return
        
        # check if snake eat itself
        if newPosition in self.position:
            self.hitMyself = True
        
        # add the new head to the position and remove the tail
        # pop the tail if we didn't eat the fruit
        self.position.append(newPosition)
        if(fruitPosition not in self.position):
            self.position.pop(0)
    
    def isSnakeHitItself(self):
        return self.hitMyself
