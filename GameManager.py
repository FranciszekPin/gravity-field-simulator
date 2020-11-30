from direct.showbase.ShowBase import ShowBase
from BallsManager import BallsManager
from SkyManager import SkyManager

class GameManager:
    def __init__(self):
        self.showBase = ShowBase()
        
        self.setCameraPosition(0, -450, 0)
        BallsManager(self.showBase)

        SkyManager(self.showBase, self.showBase.cam)

    def setCameraPosition(self, x, y, z):
        self.showBase.cam.setPos(0, -450, 0)



# execute
gameManager = GameManager()
gameManager.showBase.run()
