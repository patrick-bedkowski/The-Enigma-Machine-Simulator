from gui import EnigmaWindow
from PyQt5 import QtWidgets
import sys


def main():
    # create an app
    app = QtWidgets.QApplication(sys.argv)
    # create object of an EnigmaWindow class
    window = EnigmaWindow()
    # initiate gui window
    window.show()
    # exit application
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
