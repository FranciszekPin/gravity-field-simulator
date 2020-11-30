from direct.showbase.ShowBase import ShowBase
from BallsManager import BallsManager
from SkyManager import SkyManager

class GameManager:
    def __init__(self):
        self.showBase = ShowBase()
        
        self.setCameraPosition(0, -450, 0)
        ballsManager = BallsManager(self.showBase)

        self.makeSky()

    def setCameraPosition(self, x, y, z):
        self.showBase.cam.setPos(0, -450, 0)

    def makeSky(self):
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.skyTexture = loader.loadTexture("models/stars_1k_tex.jpg")
        self.sky.setTexture(self.skyTexture, 1)
        self.sky.reparentTo(render)
        self.sky.setScale(400)


# execute
gameManager = GameManager()
gameManager.showBase.run()
