from random import randint

class Particle:
    def __init__(self, dim, limits):
        self.dim = dim
        self.limits = limits

        self.pos = []
        self.vel = []
        self.pos.append(randint(limits[0][0], limits[0][1])) 
        self.pos.append(randint(limits[1][0], limits[1][1]))
        # TODO: further particle initialization here

    # TODO: further functions of a particlei