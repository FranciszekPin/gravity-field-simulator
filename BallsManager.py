import numpy
from direct.showbase.ShowBase import ShowBase
from panda3d.core import LPoint3, LVector3
from physics.Ball import Ball
from physics.PhysicsManager import PhysicsManager

class BallsManager:

    # every ball on the scene
    balls = []

    def __init__(self, showBase):
        self.showBase = showBase
        self.addBall(numpy.array([-3., 0., 0.]), numpy.array([0., 0., -0.09]))
        self.addBall(numpy.array([3., 0., 0.]), numpy.array([.0, 0., 0.09]))
        self.showBase.taskMgr.add(self.updateBallsTask, "updateBallsTask")
        self.lastDeltaTime = 0

    def addBall(self, position, velocity):
        self.ballModel = self.showBase.loader.loadModel("models/ball")
        self.ballModel.reparentTo(self.showBase.render)
        positionInVector3 = LVector3(position[0], position[1], position[2])
        self.ballModel.setPos(positionInVector3)
        self.balls.append(Ball(position, self.ballModel, False, velocity))

    def updateBallsPositions(self, deltaTime):
        """ Moves all balls by their velocities """
        for ball in self.balls:
            ball.move(LVector3(ball.velocity[0], ball.velocity[1], ball.velocity[2])*deltaTime)

    def updateBallsTask(self, task):
        """ Takes care of changing phsyics values of all objects """

        deltaTime = (task.time-self.lastDeltaTime)*200

        PhysicsManager().calculateForces(self.balls, deltaTime)

        # it should be called after all velocity calculations
        self.updateBallsPositions(deltaTime)

        self.lastDeltaTime = task.time

        return task.cont

