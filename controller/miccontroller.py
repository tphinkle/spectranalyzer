# Python standard library
import sys
sys.path.append('../model')
sys.path.append('../view')

# Qt
import PyQt4.QtCore
import PyQt4.QtGui


class MicController(PyQt4.QtCore.QObject):

    def __init__(self, mic_model, main_view):

        super(MicController, self).__init__()

        self._mic_model = mic_model
        self._main_view = main_view


        self.setup_connections()





    def setup_connections(self):



        self._main_view._start_button.clicked.connect(lambda: \
                self.start())

        self._main_view._stop_button.clicked.connect(lambda: \
                self.stop())




        return

    @PyQt4.QtCore.pyqtSlot()
    def start(self):



        self.connect(self._mic_model, PyQt4.QtCore.SIGNAL("new_data(PyQt_PyObject)"), self.plot_new_data)
        self._mic_model.start()


    @PyQt4.QtCore.pyqtSlot()
    def stop(self):
        print 'trying to quit'
        self._mic_model.quit()




    @PyQt4.QtCore.pyqtSlot()
    def plot_new_data(self, new_data):
        print new_data.shape
        self._main_view._main_plot_item.setData(new_data[:,0], new_data[:,1])
        return
