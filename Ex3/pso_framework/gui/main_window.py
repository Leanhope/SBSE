from PyQt5.QtWidgets import QMainWindow
from .Frame import Frame


class App(QMainWindow):
    def __init__(self, pso, parent=None):
        super(App, self).__init__(parent=parent)
        self.resolution = (800, 600)
        self.window_title = "PSO"
        self.pso = pso
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.window_title)
        self.setGeometry(200, 200, self.resolution[0], self.resolution[1])
        self.frame = Frame(pso=self.pso, parent=self)
        self.frame.start()
