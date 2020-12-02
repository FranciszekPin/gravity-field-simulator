class SkyManager:
    """ Controls background sphere """
    def __init__(self, ShowBase, camera):
        self.camera = camera
        self.sky = ShowBase.loader.loadModel("models/solar_sky_sphere")
        self.sky_tex = ShowBase.loader.loadTexture("models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.setScale(1000)
        self.sky.reparentTo(ShowBase.render)
        ShowBase.taskMgr.add(self.update_sky_position_task, "updateSkyPosition")

    def update_sky_position_task(self, task):
        """ Sets sky position the same as camera's """
        self.sky.setPos(self.camera.getPos())

        return task.cont

