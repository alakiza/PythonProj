from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from mainwindow import Ui_MainWindow
import os
import sys
from SettingsManager import SettingsManager
from SerialDevice import SerialDevice
import datetime
from MedicalDB_record import MedicalDB_record
from MedicalDB import MedicalDB

def ShowMessage(title, text, icon, buttons):
    messageBox = QtWidgets.QMessageBox()
    messageBox.setIcon(icon)
    messageBox.setWindowTitle(title)
    messageBox.setText(text)
    messageBox.setStandardButtons(buttons)
    return messageBox.exec()

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_BeginMetering.clicked.connect(self.PushButtonBeginMeteringClicked)
        self.ui.pushButton_Enter.clicked.connect(self.PushButtonEnter)
        self.ui.pushButton_Show.clicked.connect(self.PushButtonShow)
        self.ui.pushButton_AddRecord.clicked.connect(self.pushButton_AddRecordClicked)

        self.ui.action_Exit.triggered.connect(self.ActionExitTriggered)
        self.ui.action_Settings.triggered.connect(self.ActionSettingsTriggered)
        self.ui.action_SaveDB.triggered.connect(self.ActionSaveDBTriggered)
        self.ui.action_LoadDB.triggered.connect(self.ActionLoadDBTriggered)

        self.ui.action_Qt.triggered.connect(self.ActionQtTriggered)
        self.ui.action_AboutProgram.triggered.connect(self.ActionAboutTriggered)

        self.settingsManager = SettingsManager()

        self.medDB = MedicalDB(os.path.dirname(os.path.abspath(__file__))+"/DB.xml")

#Click

    def pushButton_AddRecordClicked(self):
        try:
            DateList = self.ui.lineEdit_Date.text().split('-')
            TimeList = self.ui.lineEdit_Time.text().split(':')

            self.medDB.add(self.ui.lineEdit_SurName_2.text().upper(),
                           self.ui.lineEdit_Name_2.text().upper(),
                           self.ui.lineEdit_Patronymic_2.text().upper(),
                           datetime.date(int(DateList[0]), int(DateList[1]), int(DateList[2])),
                           datetime.time(int(TimeList[0]), int(TimeList[1]), int(TimeList[2])),
                           float(self.ui.lineEdit_Temperature.text()),
                           float(self.ui.lineEdit_Pulse.text()),
                           float(self.ui.lineEdit_Systol.text()),
                           float(self.ui.lineEdit_Diastol.text()))
        except Exception as e:
            print(e)
            ShowMessage("Ошибка", "Ошибка во время добавления записи\n"+str(e), QtWidgets.QMessageBox.Warning, QtWidgets.QMessageBox.Ok)
        finally:
            self.ui.frame.setEnabled(False)
            self.ui.lineEdit_SurName_2.setEnabled(True)
            self.ui.lineEdit_Name_2.setEnabled(True)
            self.ui.lineEdit_Patronymic_2.setEnabled(True)


    def PushButtonBeginMeteringClicked(self):
        try:
            Tonometer = SerialDevice(self.settingsManager.GetPort(), self.settingsManager.GetSpeed())
            res = Tonometer.Run()
            self.ui.lineEdit_Temperature.setText(str(res[0]))
            self.ui.lineEdit_Pulse.setText(str(res[1]))
            self.ui.lineEdit_Systol.setText(str(res[2]))
            self.ui.lineEdit_Diastol.setText(str(res[3]))

            now = datetime.datetime.now()
            self.ui.lineEdit_Time.setText(str(datetime.time(now.hour, now.minute, now.second)))
            self.ui.lineEdit_Date.setText(str(datetime.date(now.year, now.month, now.day)))

            ShowMessage("Информация", "Снятие показаний завершено!", QtWidgets.QMessageBox.Information, QtWidgets.QMessageBox.Ok)
        except Exception as e:
            print(e)
            ShowMessage("Ошибка", "Произошла ошибка во время измерения!\n"+str(e), QtWidgets.QMessageBox.Warning, QtWidgets.QMessageBox.Ok)


    def PushButtonEnter(self):
        if self.medDB.Exists(self.ui.lineEdit_SurName_2.text().upper(), self.ui.lineEdit_Name_2.text().upper(), self.ui.lineEdit_Patronymic_2.text().upper()):
            self.ui.frame.setEnabled(True)
            self.ui.lineEdit_SurName_2.setEnabled(False)
            self.ui.lineEdit_Name_2.setEnabled(False)
            self.ui.lineEdit_Patronymic_2.setEnabled(False)
        else:
            reply = ShowMessage("Информация", "Пациент не найден!\nЖелаете создать нового?", QtWidgets.QMessageBox.Information, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if(reply == QtWidgets.QMessageBox.Yes):
                self.ui.frame.setEnabled(True)
                self.ui.lineEdit_SurName_2.setEnabled(False)
                self.ui.lineEdit_Name_2.setEnabled(False)
                self.ui.lineEdit_Patronymic_2.setEnabled(False)

    def PushButtonShow(self):
        self.ui.tableWidget.setRowCount(0)
        try:
            elements = self.medDB[[self.ui.lineEdit_SurName.text().upper(), self.ui.lineEdit_Name.text().upper(), self.ui.lineEdit_Patronymic.text().upper()]]
            try:
                self.ui.tableWidget.setRowCount(len(elements)/6)
                for i in range(0, len(elements), 6):
                    self.ui.tableWidget.setItem(i / 6, 0, QTableWidgetItem(elements[i+0]))
                    self.ui.tableWidget.setItem(i / 6, 1, QTableWidgetItem(elements[i+1]))
                    self.ui.tableWidget.setItem(i / 6, 2, QTableWidgetItem(elements[i+2]))
                    self.ui.tableWidget.setItem(i / 6, 3, QTableWidgetItem(elements[i+3]))
                    self.ui.tableWidget.setItem(i / 6, 4, QTableWidgetItem(elements[i+4]))
                    self.ui.tableWidget.setItem(i / 6, 5, QTableWidgetItem(elements[i+5]))
            except:
                print(e)
                ShowMessage("Информация", "Ошибка во время добавления записи в таблицу!", QtWidgets.QMessageBox.Warning, QtWidgets.QMessageBox.Ok)


        except Exception as e:
            print(e)
            ShowMessage("Информация", "Пациент не найден!", QtWidgets.QMessageBox.Warning, QtWidgets.QMessageBox.Ok)

#Menu File Actions

    def ActionSettingsTriggered(self):
        self.settingsManager.ShowDialog()

    def ActionExitTriggered(self):
        try:
            self.medDB.Save()
        except Exception as e:
            print("Error while Data base saving!\n" + str(e))
        finally:
            exit()

    def ActionSaveDBTriggered(self):
        try:
            self.medDB.Save()
            ShowMessage('Информация', 'База данных сохранена!', QtWidgets.QMessageBox.Information, QtWidgets.QMessageBox.Ok)

        except Exception as e:
            print("Error while Data base saving!\n" + str(e))
            ShowMessage('Информация', 'Ошибка во время сохранения базы данных', QtWidgets.QMessageBox.Warning, QtWidgets.QMessageBox.Ok)

    def ActionLoadDBTriggered(self):
        try:
            self.medDB.Load()
            ShowMessage('Информация', 'База данных загружена!', QtWidgets.QMessageBox.Information, QtWidgets.QMessageBox.Ok)

        except:
            ShowMessage('Информация', 'Ошибка во время загрузки базы данных', QtWidgets.QMessageBox.Warning, QtWidgets.QMessageBox.Ok)

#Menu Support Actions

    def ActionQtTriggered(self):
        app.aboutQt()

    def ActionAboutTriggered(self):
        exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())
