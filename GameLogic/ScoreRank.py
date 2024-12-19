import os 

class ScoreRank():

    scoreRankPath = os.path.join(os.path.dirname(__file__), '../Resources/gameRank.txt')

    def __init__(cls):
        pass
    
    @classmethod
    def readScoreRank(cls):
        with open(cls.scoreRankPath) as scoreRankFile:
            lines = scoreRankFile.read().split("\n")
            scores = [line for line in lines]
            return scores
    
    # @classmethod
    # def addScore(cls):
    #     with open(cls.scoreRankPath, 'w') as scoreRankFile: