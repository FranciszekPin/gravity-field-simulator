import numpy
from direct.showbase.ShowBase import ShowBase
from panda3d.core import LPoint3, LVector3
from physics.Ball import Ball
from physics.PhysicsManager import PhysicsManager

class BallsManager:

    # every ball on the scene
    balls = []

    speed = 100000

    def __init__(self, showBase):
        self.showBase = showBase

        self.addBall(numpy.array([0, 0., 0.]), numpy.array([0, 0.0, 0.0]), False, 333000, "sun")
        self.addBall(numpy.array([0., 0., 100]), numpy.array([0.0004713, 0, 0]), False, 1, "earth")
        self.addBall(numpy.array([0., 0., 50]), numpy.array([0.0006665, 0, 0]), False, 1, "mars")
        self.addBall(numpy.array([0., 0., 25]), numpy.array([0.0009426, 0, 0]), False, 1, "mercury")

        # these will orbit
        #self.addBall(numpy.array([0., 0., 0.]), numpy.array([0, 0.0, 0.0]), static = True)
        #self.addBall(numpy.array([-1.414213, -1.414213, 0]), numpy.array([0.0, 0, -0.18262]), static = False)
        self.showBase.taskMgr.add(self.updateBallsTask, "updateBallsTask")
        self.lastDeltaTime = 0
        
    def addBall(self, position, velocity, static, mass, texName):
        # Using trial and error, I have successfully determined the radius of
        # the sample model of ball and it happens to be 0.8 (what the hell)...
        ballModel = self.showBase.loader.loadModel("models/ball")
        tex = 0
        ballModel.setScale(5)

        if texName == "sun":
            tex = loader.loadTexture("models/sun_1k_tex.jpg")
            ballModel.setScale(15)
        elif texName == "earth":
            tex = loader.loadTexture("models/earth_1k_tex.jpg")
        elif texName == "mercury":
            tex = loader.loadTexture("models/mercury_1k_tex.jpg")
        elif texName == "mars":
            tex = loader.loadTexture("models/mars_1k_tex.jpg")
        elif texName == "moon":
            tex = loader.loadTexture("models/moon_1k_tex.jpg")
            ballModel.setScale(2)


        ballModel.setTexture(tex)
        # ...and therefore needs to be scaled so it's equal to 0.5
        #ballModel.setScale(1.25, 1.25, 1.25)

        ballModel.reparentTo(self.showBase.render)
        ballModel.setPos(LVector3(position[0], position[1], position[2]))
        self.balls.append(Ball(position, ballModel, static, velocity, mass))

    def updateBallsPositions(self, deltaTime):
        """ Moves all balls by their velocities """
        for ball in self.balls:
            ball.move(LVector3(ball.velocity[0], ball.velocity[1], ball.velocity[2]) * deltaTime)

    def updateBallsTask(self, task):
        """ Takes care of changing phsyics values of all objects """

        deltaTime = (task.time - self.lastDeltaTime) * self.speed

        PhysicsManager().update(self.balls, deltaTime)

        # it should be called after all velocity calculations
        self.updateBallsPositions(deltaTime)

        self.lastDeltaTime = task.time

        return task.cont
