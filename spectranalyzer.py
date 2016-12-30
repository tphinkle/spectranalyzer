# Python standard library
import sys
sys.path.append('./model')
sys.path.append('./view')
sys.path.append('./controller')


# Program specific
import mainview

import PyQt4.QtCore
import PyQt4.QtGui

class App(PyQt4.QtGui.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self._main_view = mainview.MainView()

        self._main_view.show()

def main():
    app = App(sys.argv)
    app.exec_()
    sys.exit()


if __name__ == '__main__':
    main()
