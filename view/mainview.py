# Qt stuff
import PyQt4.QtCore
import PyQt4.QtGui

print '?????'

# pyqtgraph
# import sys
#sys.path.append('~/Desktop/Programming/projects/spectranalyzer/pyqtgraph-0.9.10')

class MainView(PyQt4.QtGui.QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()

        self.setup()
        self.setup_plot()

    def setup(self):
        self._dim_x = 640
        self._dim_y = 480

        self.resize(self._dim_x, self._dim_y)

        return

    def setup_plot(self):
        self._main_plot = pg.PlotWidget(parent = self)
        self._main_plot.setLabel('bottom', text = 'Time (s)')
        self._main_plot.setLabel('left', text = 'Signal')
        self._main_plot.showGrid(x = True, y = True, alpha = 1.0)

        self._main_plot_item = pg.PlotDataItem()

        return
