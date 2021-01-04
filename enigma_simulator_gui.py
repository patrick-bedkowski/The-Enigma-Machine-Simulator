from gui import EnigmaUi, EnigmaUiCtrl
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Enigma_ui = QtWidgets.QWidget()
    ui = EnigmaUi()
    ui.setupUi(Enigma_ui)
    Enigma_ui.show()
    # Create instances of the model and controller
    EnigmaUiCtrl(ui = ui)
    # Execute program's main loop
    sys.exit(app.exec_())




