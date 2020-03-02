from physics.Ball import Ball
import numpy as np
import scipy.linalg as linalg
from math import sqrt

class PhysicsManager:
    """ Takes care of all physics stuff """

    # gravitational constant
    G = 6.6743015e-11

    def areColliding(balls):
        """ Returns True if two balls are colliding and False otherwise """

        # distance between two balls
        distance = sqrt((balls[0].position[0] - balls[1].position[0])**2 + (balls[0].position[1] - balls[1].position[1])**2 + (balls[0].position[2] - balls[1].position[2])**2)
        #print(distance)

        radiiSum = balls[0].radius + balls[1].radius

        if(distance > radiiSum):
            return False
        else:
            return True

    def calculateCollision(balls):
        # to make whole process easier to read
        a = balls[0].position
        b = balls[1].position

        print(a)
        print(b)

        mA = balls[0].mass
        mB = balls[1].mass

        vA = balls[0].velocity
        vB = balls[1].velocity

        # direction of collision
        collisionVectorA = a - b
        collisionVectorB = b - a

        # make a unit vector of direction in order to scale it after
        collisionVectorA = collisionVectorA / linalg.norm(collisionVectorA)
        collisionVectorB = collisionVectorB / linalg.norm(collisionVectorB)

        # cos(a) = (A · B) / (|A| * |B|)
        cosA = vA.dot(collisionVectorA) / linalg.norm(vA)
        cosB = vB.dot(collisionVectorB) / linalg.norm(vB)

        # calculation of scalars of:
        # vX - velocity before collision, uX - velocity after collision
        vXA = linalg.norm(vA) * cosA
        vXB = linalg.norm(vB) * cosB

        # calculation of the other component of vector v
        vYA = vA - collisionVectorA * vXA
        vYB = vB - collisionVectorB * vXB

        # velocities after collision calculated using formulas
        uXA = (mA + mB)**-1 * (2 * mB * vXB + vXA * (mA - mB))
        uXB = (uXA + vXA - vXB)

        # the final velocities, X components heading in opposite directions,
        # and Y components added to make it complete and nice and great etc
        vA = (collisionVectorA * uXA) + vYA
        vB = (collisionVectorB * uXB) + vYB

        print(vA)
        balls[0].setVelocity(vA)
        balls[1].setVelocity(vB)


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
        balls[0].updateVelocity(F * deltaTime / balls[0].mass *(-vR))
        balls[1].updateVelocity(F * deltaTime / balls[1].mass * vR)

    def update(self, balls, deltaTime):
        """ Calculates forces & velocities after collision of every pair of balls possible """

        # goes through each pair of balls, never twice and calculates forces
        i = 1
        for ball1 in balls:
            for ball2 in balls[i:]:
                #PhysicsManager.calculateForce([ball1, ball2], deltaTime)
                if(PhysicsManager.areColliding([ball1, ball2])):
                    print("FUCKING TRUE")
                    PhysicsManager.calculateCollision([ball1, ball2])
            i=i+1
