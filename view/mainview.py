# Qt stuff
import PyQt4.QtCore
import PyQt4.QtGui

# pyqtgraph
sys.path.append('./pyqtgraph-0.9.10/pyqtgraph')

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
        self._main_plot = pg.

        return
