# This Python file uses the following encoding: utf-8
from PyQt5 import QtWidgets
import datetime

class MedicalDB_record:
    def __init__(self, aDate, aTimeOfDay, aTemperature, aPulse, aSystol, aDiastol):
        self.Date = aDate
        self.TimeOfDay = aTimeOfDay
        self.Temperature = aTemperature
        self.Pulse = aPulse
        self.Systol = aSystol
        self.Diastol = aDiastol

    def __eq__(self, other):
        return ((self.Date        == other.Date)        and
                (self.TimeOfDay   == other.TimeOfDay)   and
                (self.Temperature == other.Temperature) and
                (self.Pulse       == other.Pulse)       and
                (self.Systol      == other.Systol)      and
                (self.Diastol     == other.Diastol))

    def show(self):
        print(self.Date, self.TimeOfDay, self.Temperature, self.Pulse, self.Systol, self.Diastol)
