# This Python file uses the following encoding: utf-8
from PyQt5 import QtWidgets
from PersonRecord import PersonRecord
import datetime
import xml.etree.cElementTree as xml

class XMLReader:
    def Print(self, root, level):
        print(" "*4*level, root.tag, root.attrib, root.text)

        for child in root:
            self.Print(child, level+1)

    def LoadFromFile(self, FileName):
        tree = xml.parse(FileName)
        root = tree.getroot()
        #self.Print(root, 0)

#        root = root.find("{urn:schemas-microsoft-com:office:spreadsheet}Worksheet")

#        root = root.find("{urn:schemas-microsoft-com:office:spreadsheet}Table")
#        print(" "*4, root.tag, root.attrib, root.text)

#        RowList = root.findall("{urn:schemas-microsoft-com:office:spreadsheet}Row")
#        for Row in RowList:
#            print(" "*8, Row.tag, Row.attrib, Row.text)

#            CellList = Row.findall("{urn:schemas-microsoft-com:office:spreadsheet}Cell")
#            for Cell in CellList:
#                print(" "*12, Cell.tag, Cell.attrib, Cell.text)
#                try:
#                    print(Cell.attrib['{urn:schemas-microsoft-com:office:spreadsheet}Index'])
#                except:
#                    print('ERROR')
#                for elem in Cell:
#                    print(" "*16, elem.attrib['{urn:schemas-microsoft-com:office:spreadsheet}Type'])
#                    #print(" "*16, elem.tag, elem.attrib, elem.text)
#                    print(" "*16, elem.text)

        temp = []

        root    = root.find("{urn:schemas-microsoft-com:office:spreadsheet}Worksheet")
        root    = root.find("{urn:schemas-microsoft-com:office:spreadsheet}Table")
        RowList = root.findall("{urn:schemas-microsoft-com:office:spreadsheet}Row")
        for Row in RowList:
            CellList = Row.findall("{urn:schemas-microsoft-com:office:spreadsheet}Cell")
            if (len(CellList) == 9) or (len(CellList) == 6):
                try:
                    dataJump = CellList[0].attrib['{urn:schemas-microsoft-com:office:spreadsheet}Index']
                    #print(dataJump)
                    temp.append('TRUE_5')
                except Exception as e:
                    #print(e)
                    temp.append('FALSE_0')

                for Cell in CellList:
                    for elem in Cell:
                        dataType = elem.attrib['{urn:schemas-microsoft-com:office:spreadsheet}Type']
                        dataValue = elem.text
                        #print(" "*16, dataType)
                        #print(" "*16, dataValue)

                        temp.append(dataType)
                        temp.append(dataValue)

        #print(temp)

        res = []
        try:
            i = 0
            while i < len(temp):
                #print(temp[i])
    #            print(temp[i+1])
    #            print(temp[i+2])
                #print(i, len(temp))
                if temp[i] == 'FALSE_0':
                    res.append(PersonRecord(temp[i+2].upper(), temp[i+4].upper(), temp[i+6].upper()))
                    i = i + 6
                elif temp[i] == 'TRUE_5':
                    dateList = temp[i+2].split('T')[0].split('-')
                    timeList = temp[i+4].split('T')[1].split(':')
                    timeList[2] = timeList[2].split('.')[0]
                    #print(dateList)
                    #print(timeList)
                    res[len(res)-1].add(datetime.date(int(dateList[0]), int(dateList[1]), int(dateList[2])),
                                        datetime.time(int(timeList[0]), int(timeList[1]), int(timeList[2])),
                                        float(temp[i+6]), float(temp[i+8]), float(temp[i+10]), float(temp[i+12]))
                    i = i+12
                else:
                    #print(i)
                    #print(len(temp))
                    dateList = temp[i+1].split('T')[0].split('-')
                    timeList = temp[i+3].split('T')[1].split(':')
                    timeList[2] = timeList[2].split('.')[0]
                    #print(dateList)
                    #print(timeList)
                    res[len(res)-1].add(datetime.date(int(dateList[0]), int(dateList[1]), int(dateList[2])),
                                        datetime.time(int(timeList[0]), int(timeList[1]), int(timeList[2])),
                                        float(temp[i+5]), float(temp[i+7]), float(temp[i+9]), float(temp[i+11]))

                    i=i+11
                i = i + 1
        except Exception as e:
            print(e)
        return res
