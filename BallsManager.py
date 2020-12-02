import numpy
from panda3d.core import LPoint3, LVector3
from physics.Ball import Ball
from physics.PhysicsManager import PhysicsManager


class BallsManager:
    balls = []
    speed = 100000

    def __init__(self, showBase):
        self.showBase = showBase

        self.add_balls_to_render()

        self.showBase.taskMgr.add(self.update_balls_task, "updateBallsTask")
        self.lastDeltaTime = 0

    def add_balls_to_render(self):
        """ Adds balls to simulator """
        self.add_ball(numpy.array([0., 0., 0.]), numpy.array([0, 0.0, 0.0]), True, 333000, "sun")
        self.add_ball(numpy.array([0., 0., 100]), numpy.array([0.0004713, 0, 0]), False, 1, "earth")
        self.add_ball(numpy.array([0., 0., 50]), numpy.array([0.0006665, 0, 0]), False, 1, "mars")
        self.add_ball(numpy.array([0., 0., 25]), numpy.array([0.0009426, 0, 0]), False, 1, "mercury")
        # self.addBigBall2D(0, 40, 10);

    def add_ball(self, position, velocity, static, mass, texName):
        """ Adds chosen ball to simulator """
        ball_model = self.showBase.loader.loadModel("models/ball")
        ball_model.setScale(5)

        if texName == "sun":
            tex = self.showBase.loader.loadTexture("models/sun_1k_tex.jpg")
            ball_model.setScale(15)

        elif texName == "earth":
            tex = self.showBase.loader.loadTexture("models/earth_1k_tex.jpg")
        elif texName == "mercury":
            tex = self.showBase.loader.loadTexture("models/mercury_1k_tex.jpg")
        elif texName == "mars":
            tex = self.showBase.loader.loadTexture("models/mars_1k_tex.jpg")
        elif texName == "moon":
            tex = self.showBase.loader.loadTexture("models/moon_1k_tex.jpg")
            ball_model.setScale(2)
        else:
            tex = 0
        ball_model.setTexture(tex)

        ball_model.reparentTo(self.showBase.render)
        ball_model.setPos(LVector3(position[0], position[1], position[2]))
        self.balls.append(Ball(position, ball_model, static, velocity, mass))

    def add_planet_square(self, position, radius, distance_between_balls):
        """ Colors the area with small balls """
        position = numpy.array([0, 0, 0])
        for x in numpy.arange(-radius, radius + 1e-9, distance_between_balls):
            for y in numpy.arange(-radius, radius + 1e-9, distance_between_balls):
                self.add_ball(numpy.array([x, 0.0, y]), numpy.array([0.00001, 0.0, 0.0]), False, 1000, "earth")

    def update_balls_task(self, task):
        """ Takes care of changing phsyics values of all objects """
        delta_time = (task.time - self.lastDeltaTime) * self.speed

        PhysicsManager().update(self.balls, delta_time)
        self.update_balls_positions(delta_time)

        self.lastDeltaTime = task.time

        return task.cont

    def update_balls_positions(self, delta_time):
        """ Moves all balls by their velocities """
        for ball in self.balls:
            ball.move(LVector3(ball.velocity[0], ball.velocity[1], ball.velocity[2]) * delta_time)
