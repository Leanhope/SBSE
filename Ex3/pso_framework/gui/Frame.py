from PyQt5.QtWidgets import QFrame
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QBasicTimer, QPoint


class Frame(QFrame):
    def __init__(self, pso, parent):
        super(Frame, self).__init__(parent=parent)
        self.frame_dimension = (800, 600)
        self.mouse_pos = (0, 0)
        self.pso = pso
        self.init_frame()
        self.setFixedSize(800, 600)
        self.setMouseTracking(True)

    def init_frame(self):
        self.timer = QBasicTimer()

    def mouseMoveEvent(self, event):
        self.mouse_pos = event.x(), event.y()

    def start(self):
        self.timer.start(60, self)

    def timerEvent(self, event):
        self.update()
        self.pso.update(self.mouse_pos)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.pso.draw(painter)
        self.draw_mouse(painter)

    def draw_mouse(self, painter):
        color = QColor(0, 255, 0)
        painter.setBrush(color)
        painter.setPen(QColor(0, 0, 0, 0))
        position = QPoint(self.mouse_pos[0], self.mouse_pos[1])
        painter.drawEllipse(position, 4, 4)
