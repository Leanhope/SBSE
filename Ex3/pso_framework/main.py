from PyQt5.QtWidgets import QApplication
from gui.main_window import App
from PSO import PSO
import sys


def run():
    pso = PSO(swarm_size=100,
              dim=2,
              limits=[[0, 800], [0, 600]])
    app = QApplication(sys.argv)
    gui = App(pso)
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
