import numpy
from panda3d.core import LPoint3, LVector3


class Ball:
    DEFAULT_MASS = 1e9
    STATIC_VELOCITY = numpy.array([0, 0, 0])


    def __init__(self, position, ballNode, static, velocity = STATIC_VELOCITY, mass = DEFAULT_MASS):
        self.position = position # numpy.array
        self.static = static
        self.velocity = velocity # numpy.array
        self.mass = mass
        self.ballNode = ballNode

    def move(self, translation):
        self.position += translation
        self.ballNode.setPos(LVector3(self.position[0], self.position[1], self.position[2]))

    def updateVelocity(self, velocity):
        if not self.static:
            self.velocity += numpy.array(velocity)
