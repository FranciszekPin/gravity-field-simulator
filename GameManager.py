from direct.showbase.ShowBase import ShowBase
from BallsManager import BallsManager
from SkyManager import SkyManager


class GameManager:
    def __init__(self):
        self.showBase = ShowBase()
        
        self.set_camera_position(0, -450, 0)
        BallsManager(self.showBase)

        SkyManager(self.showBase, self.showBase.cam)

    def set_camera_position(self, x, y, z):
        self.showBase.cam.setPos(0, -450, 0)


gameManager = GameManager()
gameManager.showBase.run()
