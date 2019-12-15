# This Python file uses the following encoding: utf-8
from PyQt5 import QtWidgets
import datetime
from PersonRecord import PersonRecord
from XMLReader import XMLReader
from XMLWriter import XMLWriter

class MedicalDB:
    def __init__(self, aFileName):
        self.__data = []
        self.FileName = aFileName
        print(self.FileName)
        try:
            self.LoadFromFile(aFileName)
        except Exception as e:
            print(e)
            self.__data = []
            print("Wake up, Neo\nMatrix has you")

    def __SearchRecord(self, record):
        for i in range(0, len(self.__data)):
            if(self.__data[i] == record):
                return i
        return -1

    def LoadFromFile(self, aFileName):
        xml = XMLReader()

        self.__data = xml.LoadFromFile(aFileName)

    def SaveToFile(self, aFileName):
        temp = self.getData()

        xml = XMLWriter()
        xml.WriteToFile(aFileName, temp)

    def Save(self):
        self.SaveToFile(self.FileName)

    def Load(self):
        self.LoadFromFile(self.FileName)

    def Length(self):
        return len(self.__data)

    def add(self, aSurName, aName, aPatronymic, aDate, aTimeOfDay, aTemperature, aPulse, aSystol, aDiastol):
        tmp = PersonRecord(aSurName.upper(), aName.upper(), aPatronymic.upper())
        num = self.__SearchRecord(tmp)
        if num >= 0:
            self.__data[num].add(aDate, aTimeOfDay, aTemperature, aPulse, aSystol, aDiastol)
        else:
            self.__data.append(PersonRecord(aSurName.upper(), aName.upper(), aPatronymic.upper()))
            self.__data[len(self.__data)-1].add(aDate, aTimeOfDay, aTemperature, aPulse, aSystol, aDiastol)

    def Exists(self, SurName, Name, Patronymic):
        tmp = PersonRecord(SurName.upper(), Name.upper(), Patronymic.upper())
        num = self.__SearchRecord(tmp)
        if num >= 0:
            return True
        else:
            return False

    def show(self):
        for i in range(0, len(self.__data)):
            self.__data[i].show()

    #return [SurName, Name, Patronymic, [Date, TimeOfDay, Temperature, Pulse, Systol, Diastol], .... ]
    def getData(self):
        res = []
        for i in range(0, len(self.__data)):
            res.append(str(self.__data[i].SurName.upper()))
            res.append(str(self.__data[i].Name.upper()))
            res.append(str(self.__data[i].Patronymic.upper()))
            res.append(self.__data[i].getData())

        return res

    #input list [Surname, Name, Patronymic]
    def __getitem__(self, key):
        tmp = PersonRecord(key[0], key[1], key[2])
        for i in range(0, len(self.__data)):
            if(tmp == self.__data[i]):
                return self.__data[i].getData()
        raise Exception("Пациент %s %s %s не найден", key[0], key[1], key[2])
