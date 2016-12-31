# Standard library


# Qt stuff
import PyQt4.QtCore
import PyQt4.QtGui

# pyqtgraph
import pyqtgraph as pg

class MainView(PyQt4.QtGui.QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()

        self.setup()
        self.setup_plot()
        self.setup_buttons()

    def setup(self):
        self._dim_x = 800
        self._dim_y = 600

        self.resize(self._dim_x, self._dim_y)

        return

    def setup_buttons(self):
        self._start_button = PyQt4.QtGui.QPushButton("Start", parent = self)
        self._start_button.setGeometry(0, 550, 50, 25)

        self._stop_button = PyQt4.QtGui.QPushButton("Stop", parent = self)
        self._stop_button.setGeometry(100, 550, 50, 25)

        return

    def setup_plot(self):
        self._main_plot = pg.PlotWidget(parent = self)
        self._main_plot.setLabel('bottom', text = 'Time (s)')
        self._main_plot.setLabel('left', text = 'Signal')
        self._main_plot.showGrid(x = True, y = True, alpha = 1.0)
        self._main_plot.setGeometry(0,0,640,480)

        self._main_plot_item = pg.PlotDataItem()

        self._main_plot.addItem(self._main_plot_item)

        return
