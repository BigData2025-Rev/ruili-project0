import os
import numpy as np

class GamePad:
    def __init__(self):
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
    def paint(self, snake, fruit):
        for row in self.map:
            for char in row:
                print(char, end="")
            print()

        


    