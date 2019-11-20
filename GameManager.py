from direct.showbase.ShowBase import ShowBase
from BallsManager import BallsManager

class GameManager:
    def __init__(self):
        self.showBase = ShowBase()
        self.showBase.cam.setPos(0, -25, 0)
        print("mess")
        ballsManager = BallsManager(self.showBase)

# execute
gameManager = GameManager()
gameManager.showBase.run()
