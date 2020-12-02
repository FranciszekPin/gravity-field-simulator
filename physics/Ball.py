import numpy
from panda3d.core import LVector3


class Ball:
    DEFAULT_MASS = 1e9
    STATIC_VELOCITY = numpy.array([0, 0, 0])

    def __init__(self, position, ball_node, static, velocity, mass):
        self.position = position
        self.static = static
        self.velocity = velocity
        self.mass = mass
        self.ballNode = ball_node
        self.radius = 0.4

    def move(self, translation):
        """ Change Ball position by given vector """
        if not self.static:
            self.position += translation
            self.ballNode.setPos(LVector3(self.position[0], self.position[1], self.position[2]))

    def update_velocity(self, velocity):
        """ Modify Ball velocity by given vector """
        if not self.static:
            self.velocity += numpy.array(velocity)

    def set_velocity(self, velocity):
        """ Set Ball velocity to given vector """
        if not self.static:
            self.velocity = velocity
