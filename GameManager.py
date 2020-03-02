from direct.showbase.ShowBase import ShowBase
from BallsManager import BallsManager
from SkyManager import SkyManager

class GameManager:
    def __init__(self):
        self.showBase = ShowBase()
        self.showBase.cam.setPos(0, -250, 0)
        ballsManager = BallsManager(self.showBase)
        skyManager = SkyManager(self.showBase, self.showBase.cam)

# execute
gameManager = GameManager()
gameManager.showBase.run()
