import numpy


class Ball:
    DEFAULT_MASS = 1
    STATIC_VELOCITY = numpy.array([0, 0, 0])


    def __init__(self, position, static, velocity = STATIC_VELOCITY, mass = DEFAULT_MASS):
        self.position = position # numpy.array
        self.static = static
        self.velocity = velocity # numpy.array
        self.mass = mass

    def move(self, translation):
        self.position += translation

    def setVelocity(self, velocity):
        if not static:
            self.velocity = velocity
