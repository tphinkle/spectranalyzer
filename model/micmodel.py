# Standard library
import time
import struct

# Audio
import alsaaudio
import audioop

import numpy as np

# Qt
import PyQt4.QtGui
import PyQt4.QtCore

class MicModel(PyQt4.QtCore.QThread):

    new_data = PyQt4.QtCore.pyqtSignal('PyQt_PyObject')

    def __init__(self):

        super(MicModel, self).__init__()

        self._inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)


        self._inp.setchannels(1)
        self._inp.setrate(8000)
        self._inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

        self._inp.setperiodsize(1000)

        self._keep_going = False


        self._audio_range = 2500

        self._audio_data = np.array([0 for i in range(self._audio_range)])

        self._buffer_head = 0

    def run(self):
        i = 0


        for i in range(100000):
            l,data = self._inp.read()

            data_config = np.array(struct.unpack('<'+str(len(data)/2)+'h', data))



            if self._buffer_head + l >= self._audio_range:

                self._audio_data[self._buffer_head:] = \
                    data_config[:self._audio_range - self._buffer_head]
                self._audio_data[:l - (self._audio_range - self._buffer_head)] = \
                    data_config[self._audio_range-self._buffer_head:]
            else:
                self._audio_data[self._buffer_head:self._buffer_head + l] = \
                data_config

            self._buffer_head = (self._buffer_head + l)%self._audio_range

            self._time_data = np.array([i/8000.0 for i in xrange(self._audio_data.shape[0])])

            self._data = np.hstack((self._time_data.reshape(-1,1), self._audio_data.reshape(-1,1)))

            self.emit(PyQt4.QtCore.SIGNAL('new_data(PyQt_PyObject)'), self._data)


            time.sleep(.005)

            """
    @PyQt4.QtCore.pyqtSlot()
    def start(self):

        print 'starting'

        self._keep_going = True
        self.listen()

        return
        """

    @PyQt4.QtCore.pyqtSlot()
    def stop(self):

        self._keep_going = False

        return
