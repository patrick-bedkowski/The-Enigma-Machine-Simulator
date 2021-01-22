# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.14.1

from PyQt5 import QtCore, QtGui, QtWidgets
from enigma import Enigma_interface
from enigma_class import Enigma
from PyQt5.QtGui import QPalette, QColor
# needed to format file path
import pathlib

# import needed to export, import files
from file_management import (
    create_file_txt,
    create_file_json,
    read_txt_file,
    read_json_file
)

from exceptions import (
    SteckerbrettRepeatedValues,
    SteckerbrettWrongFormat,
    SteckerbrettValueError,
    ReflectorValueIsUndefined,
    NoAsciiDetected,
    WrongNumberOfLines,
    InvalidRotorValues,
    FileNotFound,
    NoReflectorSelected,
    InvalidRotorQuantity,
    NoTextToProcess,
    UndefinedFileName,
    WrongFileName
)

class EnigmaUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.enigma_interface = Enigma_interface(Enigma)

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
        self.enigma_label.setGeometry(QtCore.QRect(10, 10, 280, 25))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.enigma_label.setFont(font)
        self.enigma_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enigma_label.setWordWrap(False)
        self.enigma_label.setObjectName("enigma_label")
        self.start_button = QtWidgets.QPushButton("red button", self, objectName="RedButton")
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
        self.steckerbrett_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.steckerbrett_label.setFont(font)
        self.steckerbrett_label.setAlignment(QtCore.Qt.AlignCenter)
        self.steckerbrett_label.setObjectName("steckerbrett_label")
        self.steckerbrett_layout.addWidget(self.steckerbrett_label)
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

        # gamma Rotor
        self.rotor_settings_layout.addLayout(self.rotor_setting_beta_layout)
        self.rotor_setting_gamma_layout = QtWidgets.QVBoxLayout()
        self.rotor_setting_gamma_layout.setSpacing(3)
        self.rotor_setting_gamma_layout.setObjectName("rotor_setting_gamma_layout")
        self.gamma_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.gamma_label.setFont(font)
        self.gamma_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.gamma_label.setObjectName("gamma_label")
        self.rotor_setting_gamma_layout.addWidget(self.gamma_label)
        self.gamma_combo = QtWidgets.QComboBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.gamma_combo.setFont(font)
        self.gamma_combo.setObjectName("gamma_combo")

        '''For each rotor, create item 26 times'''
        '''looks cleaner, then code created automatically by QTDesigner'''
        for number in range(0, 26):
            self.alpha_combo.addItem("")
            self.beta_combo.addItem("")
            self.gamma_combo.addItem("")

        # Now use a palette to switch to dark colors:
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(40, 40, 40))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.Button, QColor(255, 0, 0))
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        self.setPalette(palette)
        self.start_button.setPalette(palette)
        self.start_button.setAutoFillBackground(True)

        StyleSheet = '''
            QPushButton {
                background-color: #555;
                color: #fff;
            }
            QLabel {
                color: #ccc;
            }
            QTextBrowser {
                border: 2px solid #666;
                background-color: #555;
                color: #fff;
            }
            QComboBox {
                background-color: #555;
                color: #fff;
            }
            QVBoxLayout {
                background-color: #555;
                color: #fff;
            }
            QLineEdit {
                background-color: #555;
                color: #fff;
                border: 2px solid #666;
            }
            QHBoxLayout {
                border: 2px solid #666;
                background-color: #555;
                color: #fff;
            }
            QListView {
                border: 2px solid #666;
                background-color: #555;
                color: #fff;
            }
            '''
        self.setStyleSheet(StyleSheet)

        self.rotor_setting_gamma_layout.addWidget(self.gamma_combo)
        self.rotor_settings_layout.addLayout(self.rotor_setting_gamma_layout)
        self.rotor_layout.addLayout(self.rotor_settings_layout)
        self.retranslateUi(Enigma_ui)
        QtCore.QMetaObject.connectSlotsByName(Enigma_ui)

    def retranslateUi(self, Enigma_ui):
        _translate = QtCore.QCoreApplication.translate
        Enigma_ui.setWindowTitle("Enigma Machine Simulator")
        Enigma_ui.setWindowIcon(QtGui.QIcon('ciphering.png'))
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
        self.steckerbrett_label.setText(_translate("Enigma_ui", "Insert Steckerbrett values"))
        self.browse_button_json_label.setText(_translate("Enigma_ui", "Select .json file if you want to import settings into Enigma"))
        self.browse_button_json.setText(_translate("Enigma_ui", "Browse"))
        self.browse_button_txt_label.setText(_translate("Enigma_ui", "Select .txt file that you want to insert into Enigma"))
        self.browse_button_txt.setText(_translate("Enigma_ui", "Browse"))
        self.rotor_settings_label.setText(_translate("Enigma_ui", "Insert initial Rotors settings"))
        self.alpha_label.setText(_translate("Enigma_ui", "Alpha Rotor"))
        self.beta_label.setText(_translate("Enigma_ui", "Beta Rotor"))
        self.gamma_label.setText(_translate("Enigma_ui", "Gamma Rotor"))

        '''Set alpha, beta, gamma combo'''
        '''looks cleaner, then code created automatically by QTDesigner'''
        for number in range(0,26):
            self.alpha_combo.setItemText(number, _translate("Enigma_ui", str(number + 1)))
            self.beta_combo.setItemText(number, _translate("Enigma_ui", str(number + 1)))
            self.gamma_combo.setItemText(number, _translate("Enigma_ui", str(number + 1)))

'''
Create a Controller class to connect the GUI and the model
'''

class EnigmaWindow(EnigmaUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_operations()
        self.export_button_txt.clicked.connect(self.saveFileTxt)
        self.export_button_json.clicked.connect(self.saveFileJson)

    def main_operations(self):
        '''
        Welcoming text at the start of the program
        '''
        self.debugTextBrowser.setText(
            'Thank you for using my Enigma Machine Simulator.\nTo start:\n\
            > browse and choose file containing text\n\
            > browse and choose file containing settings or leave it blank and insert settings yourself\n\
            > click "Start Machine" button to run the program\n\
            > after certain message is showed up in this window,\n\
               you may export processed text and settings to a file\n'
        )

        '''
        Disable Export buttons until the program is initiated
        '''
        self.export_button_json.setEnabled(False)
        self.export_button_txt.setEnabled(False)
        self.export_line_json.setDisabled(True)
        self.export_line_txt.setDisabled(True)

        '''Disable line_edit where inserted path is shown after browsing a file
        Path insertion can only be done via button'''

        self.browse_line_json.setDisabled(True)
        self.browse_line_txt.setDisabled(True)

        # Set path to inserted files as empty strings
        self.txtBrowseFileName = ""
        self.jsonBrowseFileName = ""
        # GET path to inserted files
        self.browse_button_txt.clicked.connect(self.getTxtFile)
        self.browse_button_json.clicked.connect(self.getJsonFile)

        '''START ENIGMA SIMULATOR'''
        self.start_button.clicked.connect(self.run_program)

    def get_settings_from_boxes(self):
        '''
        Getting values from inserted boxes
        '''
        list_of_rotors = self.get_rotor_values_from_combo_boxes()

        # GET VALUE from STECKERBRETT EditLine
        steckerbrett = self.steckerbrett_values.text()
        # Format Steckerbrett string value into dictionary
        steckerbrett = self.enigma_interface.format_to_dict(steckerbrett)

        # if json was not imported, enable exporting
        self.export_button_json.setEnabled(True)

        # GET VALUE from REFLECTOR combobox
        reflector = self.reflector_combo.currentText()

        return list_of_rotors, steckerbrett, reflector

    def run_program(self):
        '''
        Main program.
        '''
        # Message to print after program processed data
        text_to_print = ""
        variables_collected = False

        # if user imported .json file with settings, other settings that
        # were inserted manually will not be taken into account
        if not self.jsonBrowseFileName:
            try:
                list_of_rotors, steckerbrett, reflector = self.get_settings_from_boxes()
                variables_collected = True
            except (SteckerbrettRepeatedValues, SteckerbrettWrongFormat) as Message:
                self.print_messages(Message)

        # If inserted path to .json file is not empty:
        if self.jsonBrowseFileName:
            text_to_print += 'Due to the settings being imported, settings inserted manually are not considered<br>Exporting settings is disabled<hr>'

            # if json was imported, disable exporting
            self.export_button_json.setEnabled(False)

            try:
                list_of_rotors, steckerbrett, reflector = read_json_file(self.jsonBrowseFileName)
                variables_collected = True
            except FileNotFound as Message:
                self.print_messages(Message)

        if variables_collected:
            # If inserted path to .txt file is not empty:
            try:
                ciphered_text = read_txt_file(self.txtBrowseFileName)

                # get processed text
                self.processed_text = self.process_data(list_of_rotors, steckerbrett, reflector, ciphered_text)

                text_to_print += f'Processed text: <p style="color:#2D2"><b>{self.processed_text}</b></p> If you wish to export processed data, use buttons below<br>'
                self.print_messages(text_to_print)

                # Enable EXPORT txt button
                self.export_button_txt.setEnabled(True)

                # export buttons are located in the __init__
                # because I observed multiple clicks when calling
                # button.click.connect function from here
                # it does not affect buttons being disabled
            except(
                FileNotFoundError,
                FileNotFound,
                WrongNumberOfLines,
                NoTextToProcess,
                NoAsciiDetected,
                SteckerbrettRepeatedValues,
                SteckerbrettValueError,
                ReflectorValueIsUndefined,
                InvalidRotorValues,
                NoReflectorSelected,
                InvalidRotorQuantity
            ) as Message:
                self.export_button_txt.setEnabled(False)
                self.export_button_json.setEnabled(False)
                self.print_messages(Message)

    """def observe_if_buttons_are_clicked(self):
        self.export_button_txt.clicked.connect(self.saveFileTxt)
        self.export_button_json.clicked.connect(self.saveFileJson)"""

    def process_data(self, list_of_rotors, steckerbrett, reflector, ciphered_text):
        '''Returns processed data from enigma_class'''
        self.enigma = Enigma(list_of_rotors, steckerbrett, reflector)
        processed_text = self.enigma.encryptingCodec(ciphered_text)
        return processed_text

    '''Get values inserted into combo boxes '''
    def get_rotor_values_from_combo_boxes(self):
        '''Returns list of rotors' values selected from comboboxes'''
        alpha = int(self.alpha_combo.currentText())
        beta = int(self.beta_combo.currentText())
        gamma = int(self.gamma_combo.currentText())
        return [alpha, beta, gamma]

    def print_messages(self, message):
        '''Shows text to user'''
        self.debugTextBrowser.setText(str(message))

    '''
    Browse/Import Button Functions
    '''

    def getTxtFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '', 'Text file (*.txt)')
        # show message about file
        self.browse_line_txt.setText(filename[0])
        self.txtBrowseFileName = filename[0]

    def getJsonFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '', 'Json file (*.json)')
        # show message about file
        self.browse_line_json.setText(filename[0])
        self.jsonBrowseFileName = filename[0]

    def saveFileTxt(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '', 'Text file (*.txt)')
        # show message about file
        self.export_line_txt.setText(filename[0])
        txtExportFileName = pathlib.PureWindowsPath(f'{filename[0]}').name[:-4]  # remove .txt extension, it will be added during file saving
        try:
            if txtExportFileName:
                create_file_txt(txtExportFileName, self.processed_text)
                # show message about file
                self.print_messages(f'\n{txtExportFileName}.txt file saved successfully')
        except (UndefinedFileName, WrongFileName) as Message:
            # show error message about file
            self.print_messages(Message)

    def saveFileJson(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '', 'Json file (*.json)')
        self.export_line_json.setText(filename[0])
        jsonExportFileName = pathlib.PureWindowsPath(f'{filename[0]}').name[:-5]  # remove .json extension, it will be added during file saving

        try:
            if jsonExportFileName:
                create_file_json(jsonExportFileName, self.enigma.initial_settings)
                # show message about file
                self.print_messages(f'\n{jsonExportFileName}.json file saved successfully')
        except (UndefinedFileName, WrongFileName) as Message:
            # show error message about file
            self.print_messages(Message)
