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
        for i in range(swarm_size):
            self.population.append(Particle(dim, limits))
       
        # TODO: implement further problem initialization

    def update(self, mouse_pos):
        """
        One call of update represents one iteration of the outer loop of the PSA algorithm.
        There is no return value.
        After each call of this function, the points are redrawn
        :param mouse_pos:
        """
        # TODO: implement one iteration of the PSO algorithm
        #pass

    def draw(self, painter):
        color = QColor(0, 0, 0)
        painter.setBrush(color)
        painter.setPen(QColor(0, 0, 0, 0))
        for item in self.population:
            position = QPoint(item.pos[0], item.pos[1])
            painter.drawEllipse(position, 4, 4)
