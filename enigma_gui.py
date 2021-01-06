from gui import EnigmaUi
from PyQt5 import QtWidgets
from main import enigma_interface
from enigma_class import Enigma

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Enigma_ui = QtWidgets.QWidget()
    ui = EnigmaUi()
    ui.setupUi(Enigma_ui)
    Enigma_ui.show()
    sys.exit(app.exec_())


"""class EnigmaWindow:
    def __init__(self):
        self.ui = EnigmaUi()
        self.ui.setupUi()

        # DELETE FROM THIS
        self.enigma = enigma_interface(Enigma)

        
        # if "START" button is clicked, get data
        if self.start_button_clicked:
            print('HEEE')
            self.initiate_program()
    
    def initiate_program(self):
        print(self.ui.export_data())

    '''
    def setup_settings(self):
        self.settings = self.ui'''

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = EnigmaWindow()
    window.show()
    # Create interface
   
    # Execute program's main loop
    sys.exit(app.exec_())
"""
