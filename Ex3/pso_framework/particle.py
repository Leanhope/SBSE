from random import randint

class Particle:
    def __init__(self, dim, limits):
        self.dim = dim
        self.limits = limits

        self.pos = []
        self.vel = []
        self.best = self
        self.best_info = self

        self.pos.append(randint(limits[0][0], limits[0][1])) 
        self.pos.append(randint(limits[1][0], limits[1][1]))
        self.vel.append(abs(randint(limits[0][0], limits[0][1]) - randint(limits[0][0], limits[0][1]))/2)
        self.vel.append(abs(randint(limits[1][0], limits[1][1]) - randint(limits[1][0], limits[1][1]))/2) 
        # TODO: further particle initialization here

    # TODO: further functions of a particlei