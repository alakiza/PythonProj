# This Python file uses the following encoding: utf-8
from PyQt5 import QtWidgets
from MedicalDB_record import MedicalDB_record

class PersonRecord:
    def __init__(self, aSurName, aName, aPatronymic):
        self.SurName = aSurName.upper()
        self.Name = aName.upper()
        self.Patronymic = aPatronymic.upper()
        self.__MedicalRecords = []

    def __eq__(self, other):
        return ((self.SurName.upper()     == other.SurName.upper())     and
                (self.Name.upper()        == other.Name.upper())        and
                (self.Patronymic.upper()  == other.Patronymic.upper()))

    def add(self, aDate, aTimeOfDay, aTemperature, aPulse, aSystol, aDiastol):
        self.__MedicalRecords.append(MedicalDB_record(aDate, aTimeOfDay, aTemperature, aPulse, aSystol, aDiastol))


    def show(self):
        print(self.SurName.upper(), self.Name.upper(), self.Patronymic.upper())

        for i in range(0, len(self.__MedicalRecords)):
            self.__MedicalRecords[i].show()

    def getData(self):
        res = []
        for i in range(0, len(self.__MedicalRecords)):
            res.append(str(self.__MedicalRecords[i].Date))
            res.append(str(self.__MedicalRecords[i].TimeOfDay))
            res.append(str(self.__MedicalRecords[i].Temperature))
            res.append(str(self.__MedicalRecords[i].Pulse))
            res.append(str(self.__MedicalRecords[i].Systol))
            res.append(str(self.__MedicalRecords[i].Diastol))
        return res
