from direct.showbase.ShowBase import ShowBase
from panda3d.core import LPoint3, LVector3
from physics.Ball import Ball

class SkyManager:
    """ Controls background sphere """
    def __init__(self, ShowBase, camera):
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky_tex = loader.loadTexture("models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.setScale(1000)
        self.sky.reparentTo(ShowBase.render)
        ShowBase.taskMgr.add(self.updateSkyPositionTask, "updateSkyPosition")

    def updateSkyPositionTask(self, task):
        """ Sets sky position the same as camera's """
        self.sky.setPos(camera.getPos())

        return task.cont

