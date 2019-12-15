# This Python file uses the following encoding: utf-8
from PyQt5 import QtWidgets
import sys
import os
from PyQt5.QtWidgets import *
from SettingsDialog import Ui_Dialog
import serial
import glob

class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_Cancel.clicked.connect(self.PushButtonCancelClicked)
        self.ui.pushButton_Apply.clicked.connect(self.PushButtonApplyClicked)
        self.NewPort = ''
        self.NewSpeed = ''

    def PushButtonApplyClicked(self):
        self.NewPort  = self.ui.comboBox_Port.currentText()
        self.NewSpeed = self.ui.comboBox_Speed.currentText()
        self.close()

    def PushButtonCancelClicked(self):
        self.close()


class SettingsManager:
    def __serial_ports(self):

        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def __init__(self):
        self.__port = ""
        self.__speed = ""
        self.__speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']
        self.__ports = self.__serial_ports()
        self.settingsDialog = SettingsDialog()
        if not self.TryLoadFromFile():
            if len(self.__ports) > 0:
                self.__port = self.__ports[0]

            self.__speed = "9600"
            self.SaveToFile()

    def TryLoadFromFile(self):
        try:
            self.file = open(os.path.dirname(os.path.abspath(__file__))+"/MedicalSettings.stg", 'r')
            self.__speed = file.read()
            self.__speed = file.read()
            self.file.close()
            return True
        except Exception as e:
            print(e)
            pass

    def SaveToFile(self):
        file = open(os.path.dirname(os.path.abspath(__file__))+"/MedicalSettings.stg", 'w')
        file.write(self.__port+"\n")
        file.write(self.__speed+"\n")
        file.close()


    def GetPort(self):
        return self.__port

    def GetSpeed(self):
        return self.__speed

    def ShowDialog(self):
        self.settingsDialog.ui.comboBox_Port.clear()
        self.settingsDialog.ui.comboBox_Speed.clear()
        self.settingsDialog.ui.comboBox_Speed.addItems(self.__speeds)
        self.settingsDialog.ui.comboBox_Port.addItems(self.__ports)

        for i in range(0, len(self.__ports)):
            if self.settingsDialog.ui.comboBox_Port.itemText(i) == self.__ports:
                self.settingsDialog.ui.comboBox_Port.setCurrentIndex(i)
                break

        for i in range(0, len(self.__speeds)):
            if self.settingsDialog.ui.comboBox_Speed.itemText(i) == self.__speed:
                self.settingsDialog.ui.comboBox_Speed.setCurrentIndex(i)
                break

        self.settingsDialog.exec()
        if self.settingsDialog.NewPort != '':
            self.__port = self.settingsDialog.NewPort

        if self.settingsDialog.NewSpeed != '':
            self.__speed = self.settingsDialog.NewSpeed

        self.SaveToFile()
