import os

class GamePad:
    def __init__(self):
        self.wallHit = False
        self.mapHeight = 0
        self.mapWidth = 0
        self.map = []  # 使用普通嵌套列表

    def initGameMap(self):
        # 从文件中加载地图并存储为嵌套列表
        mapFilePath = os.path.join(os.path.dirname(__file__), '../Resources/GameMap2.txt')
        with open(mapFilePath, "r", encoding="utf-8") as mapFile:
            content = mapFile.read()
            lines = content.split("\n")
            self.mapHeight = len(lines)
            self.mapWidth = len(lines[0])
            
            # 将地图存储为嵌套列表
            self.map = [list(line) for line in lines]

    # 渲染地图，包括地图、蛇和水果
    def paint(self):
        for row in self.map:
            print("".join(row))  # 将列表中的字符拼接成字符串打印

    # 更新蛇的位置
    def updateSnake(self, snakePosition):
        # 清除地图中的旧蛇位置
        for row in range(self.mapHeight):
            for col in range(self.mapWidth):
                if self.map[row][col] == "s" or self.map[row][col] == "F":
                    self.map[row][col] = " "

        # 更新蛇的新位置
        for position in snakePosition:
            if self.map[position[0]][position[1]] == "*":
                self.wallHit = True
            self.map[position[0]][position[1]] = "s"
    
    # 更新水果的位置
    def updateFruit(self, fruitPosition):
        self.map[fruitPosition[0]][fruitPosition[1]] = "F"

    # 获取地图
    def getGameMap(self):
        return self.map

    # 检查蛇是否撞墙
    def isSnakeHitWall(self):
        return self.wallHit
