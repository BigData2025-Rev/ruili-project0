import os 

class ScoreRank():

    scoreRankPath = os.path.join(os.path.dirname(__file__), '../Resources/gameRank.txt')

    def __init__(cls):
        pass
    
    @classmethod
    def readScoreRank(cls):
        with open(cls.scoreRankPath) as scoreRankFile:
            lines = scoreRankFile.read().split("\n")
            scores = [line.strip() for line in lines if line.strip().isdigit()]
            return scores
    
    @classmethod
    def showScoreRankBoard(cls):
        scores = cls.readScoreRank()
        scores = list(map(int, scores))
        scores.sort(reverse=True)
        rank = 1

        print("\n<--- Score Rank Board --->")
        for score in scores:
            if rank == 1:
                print(f"\t{score}\t1st!")
            elif rank == 2:
                print(f"\t{score}\t2nd!")
            elif rank == 3:
                print(f"\t{score}\t3rd!")
            elif rank == 6:
                print("\t...")
                break
            else:
                print(f"\t{score}")
            rank += 1
        print("<------------------------->\n")

    @classmethod
    def addScore(cls, score):
        with open(cls.scoreRankPath, 'a') as scoreRankFile:
            scoreRankFile.write(f"{score}\n")