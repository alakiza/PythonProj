# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 3)
        self.comboBox_Speed = QtWidgets.QComboBox(Dialog)
        self.comboBox_Speed.setObjectName("comboBox_Speed")
        self.gridLayout.addWidget(self.comboBox_Speed, 0, 0, 1, 3)
        self.comboBox_Port = QtWidgets.QComboBox(Dialog)
        self.comboBox_Port.setObjectName("comboBox_Port")
        self.gridLayout.addWidget(self.comboBox_Port, 1, 0, 1, 3)
        self.pushButton_Apply = QtWidgets.QPushButton(Dialog)
        self.pushButton_Apply.setObjectName("pushButton_Apply")
        self.gridLayout.addWidget(self.pushButton_Apply, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.pushButton_Cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout.addWidget(self.pushButton_Cancel, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_Apply.setText(_translate("Dialog", "Принять"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Отмена"))
