from physics.Ball import Ball
import numpy as np
import scipy.linalg as linalg

class PhysicsManager:
    """ Takes care of all physics stuff """

    # gravitational constant
    G = 6.6743015e-11

    def calculateForces(self, balls, deltaTime):
        """ Calculates forces of every pair of balls possible """

        def calculateForce(balls):
            """ Calculates gravitational force of two specific balls """

            # vector from balls[1] to balls[0]
            vR = balls[0].position - balls[1].position
            sR = linalg.norm(vR)

            # F = GMm/r^2
            F = (self.G * balls[0].mass * balls[1].mass) / (sR ** 2)

            # unit vector of R
            vR = vR/sR

            # v = Ft/m <=> F = ma
            balls[0].updateVelocity(F * deltaTime / balls[0].mass *(-vR))
            balls[1].updateVelocity(F * deltaTime / balls[1].mass * vR)

        # goes through each pair of balls, never twice and calculates forces
        i = 1 
        for ball1 in balls:
            for ball2 in balls[i:]:
                calculateForce([ball1, ball2])
            i=i+1
