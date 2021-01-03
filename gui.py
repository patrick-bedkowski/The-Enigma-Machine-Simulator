# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from main import main
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Enigma(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, Enigma_ui):
        Enigma_ui.setObjectName("Enigma_ui")
        Enigma_ui.resize(730, 740)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Enigma_ui.sizePolicy().hasHeightForWidth())
        Enigma_ui.setSizePolicy(sizePolicy)
        Enigma_ui.setMinimumSize(QtCore.QSize(730, 740))
        Enigma_ui.setMaximumSize(QtCore.QSize(730, 740))
        self.debugTextBrowser = QtWidgets.QTextBrowser(Enigma_ui)
        self.debugTextBrowser.setGeometry(QtCore.QRect(10, 470, 710, 140))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debugTextBrowser.sizePolicy().hasHeightForWidth())
        self.debugTextBrowser.setSizePolicy(sizePolicy)
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        self.enigma_label = QtWidgets.QLabel(Enigma_ui)
        self.enigma_label.setGeometry(QtCore.QRect(10, 10, 251, 25))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.enigma_label.setFont(font)
        self.enigma_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enigma_label.setWordWrap(False)
        self.enigma_label.setObjectName("enigma_label")
        self.start_button = QtWidgets.QPushButton(Enigma_ui)
        self.start_button.setGeometry(QtCore.QRect(10, 420, 711, 41))
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.layoutWidget_2 = QtWidgets.QWidget(Enigma_ui)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 670, 711, 61))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.saveJsonLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.saveJsonLayout.setContentsMargins(0, 0, 0, 0)
        self.saveJsonLayout.setObjectName("saveJsonLayout")
        self.export_button_json_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.export_button_json_label.setFont(font)
        self.export_button_json_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.export_button_json_label.setWordWrap(False)
        self.export_button_json_label.setIndent(0)
        self.export_button_json_label.setObjectName("export_button_json_label")
        self.saveJsonLayout.addWidget(self.export_button_json_label)
        self.export_json_layout = QtWidgets.QHBoxLayout()
        self.export_json_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.export_json_layout.setSpacing(8)
        self.export_json_layout.setObjectName("export_json_layout")
        self.export_line_json = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.export_line_json.setText("")
        self.export_line_json.setMaxLength(100)
        self.export_line_json.setAlignment(QtCore.Qt.AlignCenter)
        self.export_line_json.setObjectName("export_line_json")
        self.export_json_layout.addWidget(self.export_line_json)
        self.export_button_json = QtWidgets.QPushButton(self.layoutWidget_2)
        self.export_button_json.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.export_button_json.setFont(font)
        self.export_button_json.setIconSize(QtCore.QSize(18, 16))
        self.export_button_json.setObjectName("export_button_json")
        self.export_json_layout.addWidget(self.export_button_json)
        self.saveJsonLayout.addLayout(self.export_json_layout)
        self.layoutWidget = QtWidgets.QWidget(Enigma_ui)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 610, 711, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.saveTxtLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.saveTxtLayout.setContentsMargins(0, 0, 0, 0)
        self.saveTxtLayout.setObjectName("saveTxtLayout")
        self.export_button_txt_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.export_button_txt_label.setFont(font)
        self.export_button_txt_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.export_button_txt_label.setObjectName("export_button_txt_label")
        self.saveTxtLayout.addWidget(self.export_button_txt_label)
        self.export_layout_2 = QtWidgets.QHBoxLayout()
        self.export_layout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.export_layout_2.setSpacing(8)
        self.export_layout_2.setObjectName("export_layout_2")
        self.export_line_txt = QtWidgets.QLineEdit(self.layoutWidget)
        self.export_line_txt.setText("")
        self.export_line_txt.setMaxLength(100)
        self.export_line_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.export_line_txt.setObjectName("export_line_txt")
        self.export_layout_2.addWidget(self.export_line_txt)
        self.export_button_txt = QtWidgets.QPushButton(self.layoutWidget)
        self.export_button_txt.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.export_button_txt.setFont(font)
        self.export_button_txt.setIconSize(QtCore.QSize(18, 16))
        self.export_button_txt.setObjectName("export_button_txt")
        self.export_layout_2.addWidget(self.export_button_txt)
        self.saveTxtLayout.addLayout(self.export_layout_2)
        self.layoutWidget_4 = QtWidgets.QWidget(Enigma_ui)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 340, 711, 71))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.reflector_layout = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.reflector_layout.setContentsMargins(0, 0, 0, 0)
        self.reflector_layout.setObjectName("reflector_layout")
        self.rotor_settings_label_3 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rotor_settings_label_3.setFont(font)
        self.rotor_settings_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.rotor_settings_label_3.setObjectName("rotor_settings_label_3")
        self.reflector_layout.addWidget(self.rotor_settings_label_3)
        self.rotor_settings_layout_3 = QtWidgets.QHBoxLayout()
        self.rotor_settings_layout_3.setSpacing(20)
        self.rotor_settings_layout_3.setObjectName("rotor_settings_layout_3")
        self.rotor_setting_beta_layout_3 = QtWidgets.QVBoxLayout()
        self.rotor_setting_beta_layout_3.setObjectName("rotor_setting_beta_layout_3")
        self.reflector_combo = QtWidgets.QComboBox(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.reflector_combo.setFont(font)
        self.reflector_combo.setObjectName("reflector_combo")
        self.reflector_combo.addItem("")
        self.reflector_combo.addItem("")
        self.reflector_combo.addItem("")
        self.rotor_setting_beta_layout_3.addWidget(self.reflector_combo)
        self.rotor_settings_layout_3.addLayout(self.rotor_setting_beta_layout_3)
        self.reflector_layout.addLayout(self.rotor_settings_layout_3)
        self.layoutWidget1 = QtWidgets.QWidget(Enigma_ui)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 270, 711, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.steckerbrett_layout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.steckerbrett_layout.setContentsMargins(0, 0, 0, 0)
        self.steckerbrett_layout.setObjectName("steckerbrett_layout")
        self.steckerbret_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.steckerbret_label.setFont(font)
        self.steckerbret_label.setAlignment(QtCore.Qt.AlignCenter)
        self.steckerbret_label.setObjectName("steckerbret_label")
        self.steckerbrett_layout.addWidget(self.steckerbret_label)
        self.steckerbrett_values = QtWidgets.QLineEdit(self.layoutWidget1)
        self.steckerbrett_values.setObjectName("steckerbrett_values")
        self.steckerbrett_layout.addWidget(self.steckerbrett_values)
        self.layoutWidget_3 = QtWidgets.QWidget(Enigma_ui)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 110, 711, 61))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.jsonFileLayout = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.jsonFileLayout.setContentsMargins(0, 0, 0, 0)
        self.jsonFileLayout.setObjectName("jsonFileLayout")
        self.browse_button_json_label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.browse_button_json_label.setFont(font)
        self.browse_button_json_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.browse_button_json_label.setObjectName("browse_button_json_label")
        self.jsonFileLayout.addWidget(self.browse_button_json_label)
        self.browse_layout_2 = QtWidgets.QHBoxLayout()
        self.browse_layout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.browse_layout_2.setSpacing(8)
        self.browse_layout_2.setObjectName("browse_layout_2")
        self.browse_line_json = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.browse_line_json.setText("")
        self.browse_line_json.setMaxLength(100)
        self.browse_line_json.setAlignment(QtCore.Qt.AlignCenter)
        self.browse_line_json.setObjectName("browse_line_json")
        self.browse_layout_2.addWidget(self.browse_line_json)
        self.browse_button_json = QtWidgets.QPushButton(self.layoutWidget_3)
        self.browse_button_json.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.browse_button_json.setFont(font)
        self.browse_button_json.setIconSize(QtCore.QSize(18, 16))
        self.browse_button_json.setObjectName("browse_button_json")
        self.browse_layout_2.addWidget(self.browse_button_json)
        self.jsonFileLayout.addLayout(self.browse_layout_2)
        self.layoutWidget2 = QtWidgets.QWidget(Enigma_ui)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 40, 711, 61))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.txtFileLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.txtFileLayout.setContentsMargins(0, 0, 0, 0)
        self.txtFileLayout.setObjectName("txtFileLayout")
        self.browse_button_txt_label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.browse_button_txt_label.setFont(font)
        self.browse_button_txt_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.browse_button_txt_label.setObjectName("browse_button_txt_label")
        self.txtFileLayout.addWidget(self.browse_button_txt_label)
        self.browse_layout = QtWidgets.QHBoxLayout()
        self.browse_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.browse_layout.setSpacing(8)
        self.browse_layout.setObjectName("browse_layout")
        self.browse_line_txt = QtWidgets.QLineEdit(self.layoutWidget2)
        self.browse_line_txt.setText("")
        self.browse_line_txt.setMaxLength(100)
        self.browse_line_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.browse_line_txt.setObjectName("browse_line_txt")
        self.browse_layout.addWidget(self.browse_line_txt)
        self.browse_button_txt = QtWidgets.QPushButton(self.layoutWidget2)
        self.browse_button_txt.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.browse_button_txt.setFont(font)
        self.browse_button_txt.setIconSize(QtCore.QSize(18, 16))
        self.browse_button_txt.setObjectName("browse_button_txt")
        self.browse_layout.addWidget(self.browse_button_txt)
        self.txtFileLayout.addLayout(self.browse_layout)
        self.layoutWidget3 = QtWidgets.QWidget(Enigma_ui)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 170, 711, 91))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.rotor_layout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.rotor_layout.setContentsMargins(0, 0, 0, 0)
        self.rotor_layout.setObjectName("rotor_layout")
        self.rotor_settings_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rotor_settings_label.setFont(font)
        self.rotor_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rotor_settings_label.setObjectName("rotor_settings_label")
        self.rotor_layout.addWidget(self.rotor_settings_label)
        self.rotor_settings_layout = QtWidgets.QHBoxLayout()
        self.rotor_settings_layout.setSpacing(20)
        self.rotor_settings_layout.setObjectName("rotor_settings_layout")
        self.rotor_setting_alpha_layout = QtWidgets.QVBoxLayout()
        self.rotor_setting_alpha_layout.setSpacing(3)
        self.rotor_setting_alpha_layout.setObjectName("rotor_setting_alpha_layout")

        # Alpha Rotor
        self.alpha_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.alpha_label.setFont(font)
        self.alpha_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.alpha_label.setObjectName("alpha_label")
        self.rotor_setting_alpha_layout.addWidget(self.alpha_label)
        self.alpha_combo = QtWidgets.QComboBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.alpha_combo.setFont(font)
        self.alpha_combo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.alpha_combo.setObjectName("alpha_combo")
        self.rotor_setting_alpha_layout.addWidget(self.alpha_combo)
        self.rotor_settings_layout.addLayout(self.rotor_setting_alpha_layout)

        # Beta Rotor
        self.rotor_setting_beta_layout = QtWidgets.QVBoxLayout()
        self.rotor_setting_beta_layout.setSpacing(3)
        self.rotor_setting_beta_layout.setObjectName("rotor_setting_beta_layout")
        self.beta_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.beta_label.setFont(font)
        self.beta_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.beta_label.setObjectName("beta_label")
        self.rotor_setting_beta_layout.addWidget(self.beta_label)
        self.beta_combo = QtWidgets.QComboBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.beta_combo.setFont(font)
        self.beta_combo.setObjectName("beta_combo")
        self.rotor_setting_beta_layout.addWidget(self.beta_combo)

        # Gama Rotor
        self.rotor_settings_layout.addLayout(self.rotor_setting_beta_layout)
        self.rotor_setting_gama_layout = QtWidgets.QVBoxLayout()
        self.rotor_setting_gama_layout.setSpacing(3)
        self.rotor_setting_gama_layout.setObjectName("rotor_setting_gama_layout")
        self.gama_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.gama_label.setFont(font)
        self.gama_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.gama_label.setObjectName("gama_label")
        self.rotor_setting_gama_layout.addWidget(self.gama_label)
        self.gama_combo = QtWidgets.QComboBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.gama_combo.setFont(font)
        self.gama_combo.setObjectName("gama_combo")

        '''
        Welcoming text at the start of the program
        '''
        self.debugTextBrowser.setText(
            'Thank you for using my Enigma Machine Simulator.\nTo start:\n\
            > browse and choose file containing text\n\
            > browse and choose file containing settings or leave it blank and insert settings yourself\n\
            > click "Start Machine" button to run the program\n\
            > after certain message is showed in this window,\n\
               you may export ciphered text and settings to a file\n'
        )

        '''
        Disable Export buttons unit the program is running
        '''
        self.export_button_json.setEnabled(False)
        self.export_button_txt.setEnabled(False)

        '''For each rotor, create item 26 times'''
        '''looks cleaner, then code created automatically by QTDesigner'''
        for number in range(0,26):
            self.alpha_combo.addItem("")
            self.beta_combo.addItem("")
            self.gama_combo.addItem("")

        self.rotor_setting_gama_layout.addWidget(self.gama_combo)
        self.rotor_settings_layout.addLayout(self.rotor_setting_gama_layout)
        self.rotor_layout.addLayout(self.rotor_settings_layout)

        self.retranslateUi(Enigma_ui)
        QtCore.QMetaObject.connectSlotsByName(Enigma_ui)

        '''
        Browse files
        '''
        txtBrowseFileName = self.browse_button_txt.clicked.connect(self.getTxtFile)
        jsonBrowseFileName = self.browse_button_json.clicked.connect(self.getJsonFile)

        '''
        Export files
        '''
        tsonExportFileName = self.export_button_json.clicked.connect(self.getSaveFileNameJson)
        txtExportFileName = self.export_button_txt.clicked.connect(self.getSaveFileNameTxt)

        # When clicked enigma simulator is running
        self.start_button.clicked.connect(self.runProgram)


    def runProgram(self):





        # Enable buttons, AT THE BOTTOM
        self.export_button_json.setEnabled(True)
        self.export_button_txt.setEnabled(True)

    '''
        Browse/Import Button Functions
    '''

    def getTxtFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '','Text file (*.txt)')
        self.browse_line_txt.setText(filename[0])
        return filename

    def getJsonFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '','Json file (*.json)')
        self.browse_line_json.setText(filename[0])
        return filename

    def getSaveFileNameTxt(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '','Text file (*.txt)')
        self.export_line_txt.setText(filename[0])
        return filename

    def getSaveFileNameJson(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '','Json file (*.json)')
        self.export_line_json.setText(filename[0])
        return filename

    def retranslateUi(self, Enigma_ui):
        _translate = QtCore.QCoreApplication.translate
        Enigma_ui.setWindowTitle(_translate("Enigma_ui", "Enigma_ui"))
        self.enigma_label.setText(_translate("Enigma_ui", "Enigma Machine Simulator"))
        self.start_button.setText(_translate("Enigma_ui", "START MACHINE"))
        self.export_button_json_label.setText(_translate("Enigma_ui", "Save Enigma settings into .json file"))
        self.export_button_json.setText(_translate("Enigma_ui", "Export"))
        self.export_button_txt_label.setText(_translate("Enigma_ui", "Save ciphered message into .txt file"))
        self.export_button_txt.setText(_translate("Enigma_ui", "Export"))
        self.rotor_settings_label_3.setText(_translate("Enigma_ui", "Insert Reflector value"))
        self.reflector_combo.setItemText(0, _translate("Enigma_ui", "A"))
        self.reflector_combo.setItemText(1, _translate("Enigma_ui", "B"))
        self.reflector_combo.setItemText(2, _translate("Enigma_ui", "C"))
        self.steckerbret_label.setText(_translate("Enigma_ui", "Insert Steckerbrett values"))
        self.browse_button_json_label.setText(_translate("Enigma_ui", "Select .json file if you want to import settings into Enigma"))
        self.browse_button_json.setText(_translate("Enigma_ui", "Browse"))
        self.browse_button_txt_label.setText(_translate("Enigma_ui", "Select .txt file that you want to insert into Enigma"))
        self.browse_button_txt.setText(_translate("Enigma_ui", "Browse"))
        self.rotor_settings_label.setText(_translate("Enigma_ui", "Insert initial Rotors settings"))
        self.alpha_label.setText(_translate("Enigma_ui", "Alpha Rotor"))
        self.beta_label.setText(_translate("Enigma_ui", "Beta Rotor"))
        self.gama_label.setText(_translate("Enigma_ui", "Gama Rotor"))

        '''Set alpha, beta, gama combo'''
        '''looks cleaner, then code created automatically by QTDesigner'''
        for number in range(0,26):
            self.alpha_combo.setItemText(number, _translate("Enigma_ui", f"{number+1}"))
            self.beta_combo.setItemText(number, _translate("Enigma_ui", f"{number+1}"))
            self.gama_combo.setItemText(number, _translate("Enigma_ui", f"{number+1}"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Enigma_ui = QtWidgets.QWidget()
    ui = Ui_Enigma()
    ui.setupUi(Enigma_ui)
    Enigma_ui.show()
    sys.exit(app.exec_())
