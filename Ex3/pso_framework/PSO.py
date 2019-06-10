from math import hypot
import random
from particle import Particle
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPoint



class PSO:
    def __init__(self, swarm_size, dim, limits, params=[0.75, .4, .5, .6, 0.05]):
        """
        TODO: play around with the default parameters in the argument list
        :param swarm_size: integer, defining how many individuals the population holds
        :param dim: dimension of the problem (for visualization 2 is used)
        :param limits: array defining the limits for each dimension (eg. for 2 dims: [[x_min, x_max], [y_min, y_max]])
        :param params: [alpha, beta, gamma, delta, epsilon] default=[0.75, 0.4, 0.5, 0.6, 0.05]
        """
        self.alpha = params[0]
        self.beta = params[1]
        self.gamma = params[2]
        self.delta = params[3]
        self.epsilon = params[4]
        self.dim = dim
        self.limits = limits
        self.population = []
        self.swarm_size = swarm_size
        for i in range(self.swarm_size):
            self.population.append(Particle(dim, limits))
       
        self.best_particle = self.population[0]
        self.mouse_pos_old = [0.0, 0.0]
        # TODO: implement further problem initialization

    def update(self, mouse_pos):
        """
        One call of update represents one iteration of the outer loop of the PSA algorithm.
        There is no return value.
        After each call of this function, the points are redrawn
        :param mouse_pos:
        """

        for p in self.population:
            fitness = self.assess_fitness(p, mouse_pos)
            if fitness < self.assess_fitness(self.best_particle, mouse_pos):self.best_particle = p
            if fitness < self.assess_fitness(p.best, mouse_pos):p.best = p
            for i in range(int(self.swarm_size/20)):
                rand_p = self.population[random.randint(0, self.swarm_size - 1)]
                fitness_rand = self.assess_fitness(rand_p, mouse_pos)
                if fitness_rand < self.assess_fitness(p.best_info, mouse_pos):p.best_info = rand_p
            for i in range(self.dim):
                b = random.uniform(0.0, self.beta)
                c = random.uniform(0.0, self.gamma)
                d = random.uniform(0.0, self.delta)
                p.vel[i] = self.alpha * p.vel[i] + b * (p.best.pos[i] - p.pos[i]) + c * (p.best_info.pos[i] - p.pos[i]) + d * (self.best_particle.pos[i] - p.pos[i])
              
        for p in self.population:
            for i in range(self.dim):
                p.pos[i] += self.epsilon * p.vel[i]
        
        self.mouse_pos_old = mouse_pos


    def draw(self, painter):
        color = QColor(0, 0, 0)
        painter.setBrush(color)
        painter.setPen(QColor(0, 0, 0, 0))
        for item in self.population:
            position = QPoint(item.pos[0], item.pos[1])
            painter.drawEllipse(position, 4, 4)
    
    def assess_fitness(self, Particle, pos):
        return hypot(Particle.pos[0] - pos[0], Particle.pos[1] - pos[1])