#!/usr/local/python/bin/python
# coding=utf-8

import sys
<<<<<<< HEAD
from PyQt6 import QtGui
=======
from PyQt4 import QtGui
>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9


def main():

    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Test')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
