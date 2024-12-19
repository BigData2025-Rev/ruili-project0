class Snake:
    def __init__(self):
        self.position = []
        self.hitMyself = False
        self.pervDirection = ""
    
    def initPosition(self, gameMap):
        initX = len(gameMap) // 2
        initY = len(gameMap[0]) // 2
        if gameMap[initX][initY] != " ":
            initX -= 1
        self.position.append([initX, initY])

    def getPosition(self):
        return self.position
    
    def move(self, direction, fruitPosition):
        direction = direction.upper()

        # if snake try to move to oppsite direction, do not move
        if (direction == "W" and self.pervDirection == "S") or \
            (direction == "S" and self.pervDirection == "W") or \
            (direction == "A" and self.pervDirection == "D") or \
            (direction == "D" and self.pervDirection == "A"):
                return
        # if user input illegal, just move as pervious direction
        if len(direction) == 0 or not direction in "WASD":
            direction = self.pervDirection

        if direction == "W":
            newPosition = [self.position[-1][0]-1, self.position[-1][1]]
        elif direction == "A":
            newPosition = [self.position[-1][0], self.position[-1][1]-1]
        elif direction == "S":
            newPosition = [self.position[-1][0]+1, self.position[-1][1]]
        elif direction == "D":
            newPosition = [self.position[-1][0], self.position[-1][1]+1]
        else:
            return
        
        self.pervDirection = direction

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
