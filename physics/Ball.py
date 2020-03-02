import numpy
from panda3d.core import LPoint3, LVector3


class Ball:
    DEFAULT_MASS = 1e9
    STATIC_VELOCITY = numpy.array([0, 0, 0])

    def __init__(self, position, ballNode, static, velocity, mass):
        self.position = position # numpy.array
        self.static = static
        self.velocity = velocity # numpy.array
        self.mass = mass
        self.ballNode = ballNode
        self.radius = 0.4

        print(static)
        print(velocity)
        print(mass)
        print("---")

    def move(self, translation):
        if not self.static:
            self.position += translation
            self.ballNode.setPos(LVector3(self.position[0], self.position[1], self.position[2]))

    def updateVelocity(self, velocity):
        if not self.static:
            self.velocity += numpy.array(velocity)

    def setVelocity(self, velocity):
        if not self.static:
            self.velocity = velocity
