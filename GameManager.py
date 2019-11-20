from direct.showbase.ShowBase import ShowBase
from BallsManager import BallsManager

class GameManager:
    def __init__(self):
        self.showBase = ShowBase()
        self.showBase.cam.setPos(0, -25, 0)
        ballsManager = BallsManager(self.showBase)
        self.makeSky()

    def makeSky(self):
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky_tex = loader.loadTexture("models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.reparentTo(render)
        self.sky.setScale(40)


# execute
gameManager = GameManager()
gameManager.showBase.run()
