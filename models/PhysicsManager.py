from physics.Ball import Ball
import numpy as np
import scipy.linalg as linalg
from math import sqrt

class PhysicsManager:
    """ Takes care of all physics stuff """

    # gravitational constant
    G = 6.6743015e-11


    def calculateForce(balls, deltaTime):
        """ Calculates gravitational force of two specific balls """

        # vector from balls[1] to balls[0]
        vR = balls[0].position - balls[1].position

        sR = linalg.norm(vR)

        # TODO --------
        if sR == 0:
            return

        # F = GMm/r^2
        F = (PhysicsManager.G * balls[0].mass * balls[1].mass) / (sR ** 2)

        # unit vector of R
        vR = vR/sR

        # v = Ft/m <=> F = ma
        balls[0].update_velocity(F * deltaTime / balls[0].mass * (-vR))
        balls[1].update_velocity(F * deltaTime / balls[1].mass * vR)

    def update(self, balls, deltaTime):
        """ Calculates forces & velocities after collision of every pair of balls possible """

        # goes through each pair of balls, never twice and calculates forces
        i = 1
        for ball1 in balls:
            for ball2 in balls[i:]:
                PhysicsManager.calculateForce([ball1, ball2], deltaTime)
            i=i+1
