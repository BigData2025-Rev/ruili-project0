import os 
import json
from datetime import datetime, timezone
from .ANSI import ANSI

class UserAccount():

    currentAccount = None
    scoreRankPath = os.path.join(os.path.dirname(__file__), '../Resources/gameRank.json')
    userAccountPath = os.path.join(os.path.dirname(__file__), '../Resources/userAccount.json')

    def __init__(cls):
        pass

    @classmethod
    def readUserAccount(cls):
        try:
            with open(cls.userAccountPath, 'r', encoding='utf-8') as userAccountFile:
                accountList = json.load(userAccountFile)
                return accountList
        except FileNotFoundError:
            print("userAccount file not found!")
            return []
        except json.JSONDecodeError:
            print("Error decoding the JSON file!")
            return []


    @classmethod
    def readScoreRank(cls):
        try:
            with open(cls.scoreRankPath, 'r', encoding='utf-8') as scoreRankFile:
                scores = json.load(scoreRankFile)
                return scores
        except FileNotFoundError:
            print("Score rank file not found!")
            return []
        except json.JSONDecodeError:
            print("Error decoding the JSON file!")
            return []

    @classmethod
    def isLoggedIn(cls):
        return not cls.currentAccount is None

    @classmethod
    def login(cls):
        if cls.isLoggedIn():
            print(f"{ANSI.BOLD}You already logged in!{ANSI.RESET}")
            return
        
        accountList = cls.readUserAccount()
        retry = 0
        while(retry < 3):
            username = input(f"{ANSI.BOLD}{ANSI.YELLOW}Please enter your username: {ANSI.RESET}")
            password = input(f"{ANSI.BOLD}{ANSI.YELLOW}Please enter your password: {ANSI.RESET}")
            for account in accountList:
                if account["username"] == username and account["password"] == password:
                    cls.currentAccount = username
                    print(f"{ANSI.BOLD}You logged in as {username}{ANSI.RESET}")
                    return
            print(f"{ANSI.BOLD}The account or password is wrong, please try again!\n{ANSI.RESET}")
            retry += 1
        
        print(f"{ANSI.BOLD}{ANSI.RED}You failed too many times!{ANSI.RESET}")
        return

    @classmethod
    def register(cls):
        accountList = cls.readUserAccount()
        while True:
            username = input(f"{ANSI.BOLD}{ANSI.YELLOW}Please enter your username: {ANSI.RESET}")
            if any(account["username"] == username for account in accountList):
                print(f"{ANSI.BOLD}{ANSI.RED}The username already exists: {username}{ANSI.RESET}")
            else:
                break

        while True:
            password = input(f"{ANSI.BOLD}{ANSI.YELLOW}Please enter your password: {ANSI.RESET}")
            if password.isalnum() and len(password) <= 10:
                break
            print(f"{ANSI.BOLD}{ANSI.RED}Password must be alphanumeric and no more than 10 characters.{ANSI.RESET}")

        newAccount = {"username": username, "password": password}
        accountList.append(newAccount)

        with open(cls.userAccountPath, 'w', encoding='utf-8') as userAccountFile:
            json.dump(accountList, userAccountFile, indent=4, ensure_ascii=False)

        print(f"{ANSI.BOLD}{ANSI.GREEN}Registration successful!{ANSI.RESET}")
    
    @classmethod
    def logout(cls):
        pass
    
    @classmethod
    def showScoreRankBoard(cls):
        scores = cls.readScoreRank()
        # sort the rank board, score first, then date
        scores = sorted(scores, key=lambda x: (x["score"], x["date"]), reverse=True)
        rank = 1

        RESET = "\033[0m"
        BOLD = "\033[1m"
        ITALIC = "\033[3m"
        RED = "\033[31m"
        GREEN = "\033[32m"
        BLUE = "\033[34m"
        CYAN = "\033[36m"
        YELLOW = "\033[33m"

        print(f"\n{BOLD}{CYAN}<-------------------- Score Rank Board ----------------------->{RESET}")
        print(f"{BOLD}\tUSER\t|\tSCORE\t|\tDATE{RESET}")
        
        for score in scores:
            username_style = f"{BOLD}{GREEN}"
            score_style = f"{YELLOW}"
            date_style = f"{ITALIC}{RED}" 

            print(f"\t{username_style}{score['username']}{RESET}\t|"
                  f"\t{score_style}{score['score']}{RESET}\t|"
                  f"\t{date_style}{score['date']}{RESET}")
            
            if rank == 8:
                print(f"\t{username_style}...{RESET}\t|"
                  f"\t{score_style}...{RESET}\t|"
                  f"\t{date_style}...{RESET}")
                break
            rank += 1

        print(f"{BOLD}{CYAN}<------------------------------------------------------------>{RESET}\n")

    @classmethod
    def addScore(cls, score: int):

        # if user didn't login, stop add new score
        if cls.currentAccount is None:
            print(f"{ANSI.BOLD}{ANSI.RED}You need to log in before adding a score!{ANSI.RESET}")
            return

        newScore = {
            "username": cls.currentAccount,
            "score": score,
            "date": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        }
        scores = cls.readScoreRank()
        scores.append(newScore)
        with open(cls.scoreRankPath, 'w', encoding='utf-8') as scoreRankFile:
            json.dump(scores, scoreRankFile, indent=4, ensure_ascii=False)