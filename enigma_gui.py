from gui import EnigmaUi, EnigmaWindow
from PyQt5 import QtWidgets
#from main import enigma_interface
from enigma_class import Enigma

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #Enigma_ui = QtWidgets.QWidget()
    """ui = EnigmaUi()
    ui.setupUi(Enigma_ui)"""
    window = EnigmaWindow()
    window.show()

    #Enigma_ui.show()
    sys.exit(app.exec_())
