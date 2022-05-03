from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)


def do_calc(names: list, prices: list):
    labels = names
    numbers = prices

    index = np.arange(len(labels))
    plt.figure(figsize=(10, 5))
    plt.barh(index, numbers)
    for i, v in enumerate(numbers):
        plt.text(v + 0.2, i, str(v), color='black', fontweight='bold')
    plt.yticks(index, labels, fontsize=10, rotation=0)
    plt.title("Cars Price from https://www.trademe.co.nz/a/motors/cars/bmw/")
    plt.show()


class Window(QMainWindow):
    def __init__(self, names: list, prices: list, parent=None):
        super(Window, self).__init__(parent)
        self.names = names
        self.prices = prices

        self.title_label = QLabel("Label Text")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        lay = QVBoxLayout(central_widget)
        lay.addWidget(self.title_label)

        plt.ion()
        do_calc(self.names, self.prices)

        for tl in QApplication.topLevelWidgets():
            if isinstance(tl, QMainWindow) and isinstance(
                    tl.centralWidget(), FigureCanvas
            ):
                lay.addWidget(tl)
