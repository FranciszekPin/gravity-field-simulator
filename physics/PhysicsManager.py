import scipy.linalg as linalg


class PhysicsManager:
    """ Takes care of all physics stuff """

    # gravitational constant
    G = 6.6743015e-11

    def calculate_force(self, balls, deltaTime):
        """ Calculates gravitational force of two specific balls """

        v_r = balls[0].position - balls[1].position

        sR = linalg.norm(v_r)

        # F = GMm/r^2
        if sR == 0:
            return
        F = (PhysicsManager.G * balls[0].mass * balls[1].mass) / (sR ** 2)

        # unit vector of R
        v_r = v_r / sR

        # v = Ft/m <=> F = ma
        balls[0].update_velocity(F * deltaTime / balls[0].mass * (-v_r))
        balls[1].update_velocity(F * deltaTime / balls[1].mass * v_r)

    def update(self, balls, delta_time):
        """ Calculates forces of every pair of balls """
        i = 1
        for ball1 in balls:
            for ball2 in balls[i:]:
                PhysicsManager.calculate_force(self, [ball1, ball2], delta_time)
            i = i + 1
