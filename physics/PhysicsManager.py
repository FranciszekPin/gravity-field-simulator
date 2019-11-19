from Ball import Ball
import numpy as np
import scipy.linalg as linalg

class PhysicsManager:
""" Takes care of all physics stuff """

    # gravitational constant
    G = 6.6743015e-11

    # this needs to be changed everytime when any of these functions are called
    deltaTime = 0

    def calculateForces(self, balls):
    """ Calculates forces of every pair of balls possible """

        def calculateForce(balls):
            """ Calculates gravitational force of two specific balls """

            # vector from balls[1] to balls[0]
            vR = balls[0] - balls[1]
            sR = linalg.norm(vR)

            # F = GMm/r^2
            F = G * balls[0].mass * balls[1].mass / (linalg.norm(sR)) ** 2

            # unit vector of R
            vR = vR/R

            # v = Ft/m <=> F = ma
            balls[0].move(F * deltaTime / balls[0].mass *(-vR))
            balls[1].move(F * deltaTime / balls[1].mass * vR)

        # goes through each pair of balls, never twice and calculates forces
        i = 0
        for ball1 in balls:
            for ball2 in balls[i:]:
                calculateForce([ball1, ball2])
            i++
