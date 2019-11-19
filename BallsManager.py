import numpy
from direct.showbase.ShowBase import ShowBase
from panda3d.core import LPoint3, LVector3
from physics.Ball import Ball

class BallsManager:

    # every ball on the scene
    balls = []

    def __init__(self, showBase):
        self.showBase = showBase
        self.addBall(numpy.array([1, 1, 1]), numpy.array([1, 1, 1]))

    def addBall(self, position, velocity):
        self.balls.append(Ball(position, False, numpy.array([0.1, 0.1, 0])))
        print(self.balls)
        self.ballModel = self.showBase.loader.loadModel("models/ball")
        self.ballModel.reparentTo(self.showBase.render)
        position = LVector3(position[0], position[1], position[2])
        self.ballModel.setPos(position)
