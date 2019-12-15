# This Python file uses the following encoding: utf-8
from PyQt5 import QtWidgets
from PersonRecord import PersonRecord
import datetime
import xml.etree.cElementTree as xml

class XMLWriter:
    def WriteToFile(self, FileName, data):
        root = xml.Element('Workbook', {'xmlns'     : "urn:schemas-microsoft-com:office:spreadsheet",
                                        'xmlns:c'   : "urn:schemas-microsoft-com:office:component:spreadsheet",
                                        'xmlns:html': "http://www.w3.org/TR/REC-html40",
                                        'xmlns:o'   : "urn:schemas-microsoft-com:office:office",
                                        'xmlns:ss'  : "urn:schemas-microsoft-com:office:spreadsheet",
                                        'xmlns:x2'  : "http://schemas.microsoft.com/office/excel/2003/xml",
                                        'xmlns:x'   : "urn:schemas-microsoft-com:office:excel",
                                        'xmlns:xsi' : "http://www.w3.org/2001/XMLSchema-instance"})

        tree = xml.ElementTree(root)

        OfficeDocumentSettings = xml.SubElement(root, 'OfficeDocumentSettings', {'xmlns':"urn:schemas-microsoft-com:office:office"})
        Colors = xml.SubElement(OfficeDocumentSettings, 'Colors', {})

        Color = xml.SubElement(Colors, 'Color', {})
        Index = xml.SubElement(Color, 'Index', {})
        Index.text = '3'
        RGB = xml.SubElement(Color, 'RGB', {})
        RGB.text = '#000000'

        Color = xml.SubElement(Colors, 'Color', {})
        Index = xml.SubElement(Color, 'Index', {})
        Index.text = '4'
        RGB = xml.SubElement(Color, 'RGB', {})
        RGB.text = '#0000ee'

        Color = xml.SubElement(Colors, 'Color', {})
        Index = xml.SubElement(Color, 'Index', {})
        Index.text = '5'
        RGB = xml.SubElement(Color, 'RGB', {})
        RGB.text = '#006600'

        Color = xml.SubElement(Colors, 'Color', {})
        Index = xml.SubElement(Color, 'Index', {})
        Index.text = '6'
        RGB = xml.SubElement(Color, 'RGB', {})
        RGB.text = '#333333'

        Color = xml.SubElement(Colors, 'Color', {})
        Index = xml.SubElement(Color, 'Index', {})
        Index.text = '7'
        RGB = xml.SubElement(Color, 'RGB', {})
        RGB.text = '#808080'

        Color = xml.SubElement(Colors, 'Color', {})
        Index = xml.SubElement(Color, 'Index', {})
        Index.text = '8'
        RGB = xml.SubElement(Color, 'RGB', {})
        RGB.text = '#996600'

        Color = xml.SubElement(Colors, 'Color', {})
        Index = xml.SubElement(Color, 'Index', {})
        Index.text = '9'
        RGB = xml.SubElement(Color, 'RGB', {})
        RGB.text = '#c0c0c0'

        Color = xml.SubElement(Colors, 'Color', {})
        Index = xml.SubElement(Color, 'Index', {})
        Index.text = '10'
        RGB = xml.SubElement(Color, 'RGB', {})
        RGB.text = '#cc0000'

        Color = xml.SubElement(Colors, 'Color', {})
        Index = xml.SubElement(Color, 'Index', {})
        Index.text = '11'
        RGB = xml.SubElement(Color, 'RGB', {})
        RGB.text = '#ffffff'

        ExcelWorkbook = xml.SubElement(root, 'ExcelWorkbook', {'xmlns':'urn:schemas-microsoft-com:office:excel'})
        WindowHeight = xml.SubElement(ExcelWorkbook, 'WindowHeight', {})
        WindowHeight.text = '9000'
        WindowWidth = xml.SubElement(ExcelWorkbook, 'WindowWidth', {})
        WindowWidth.text = '13860'

        WindowTopX = xml.SubElement(ExcelWorkbook, 'WindowTopX', {})
        WindowTopX.text = '240'
        WindowTopY = xml.SubElement(ExcelWorkbook, 'WindowTopY', {})
        WindowTopY.text = '75'

        ProtectStructure = xml.SubElement(ExcelWorkbook, 'ProtectStructure', {})
        ProtectStructure.text = 'False'

        ProtectWindows = xml.SubElement(ExcelWorkbook, 'ProtectWindows', {})
        ProtectWindows.text = 'False'

        Styles = xml.SubElement(root, 'Styles', {})
        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Default", 'ss:Name':"Default"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Heading_20__28_user_29_", 'ss:Name':"Heading (user)"})
        Font = xml.SubElement(Style, 'Font', {'ss:Bold':"1", 'ss:Color':"#000000", 'ss:Size':"24"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Heading_20_1", 'ss:Name':"Heading 1"})
        Font = xml.SubElement(Style, 'Font', {'ss:Bold':"1", 'ss:Color':"#000000", 'ss:Size':"18"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Heading_20_2", 'ss:Name':"Heading 2"})
        Font = xml.SubElement(Style, 'Font', {'ss:Bold':"1", 'ss:Color':"#000000", 'ss:Size':"12"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Text", 'ss:Name':"Text"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Note", 'ss:Name':"Note"})
        Font = xml.SubElement(Style, 'Font', {'ss:Color':"#333333", 'ss:Size':"10"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Footnote", 'ss:Name':"Footnote"})
        Font = xml.SubElement(Style, 'Font', {'ss:Color':"#808080", 'ss:Italic':"1", 'ss:Size':"10"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Hyperlink", 'ss:Name':"Hyperlink"})
        Font = xml.SubElement(Style, 'Font', {'ss:Color':"#0000ee", 'ss:Size':"10", 'ss:Underline':"Single"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Status", 'ss:Name':"Status"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Good", 'ss:Name':"Good"})
        Font = xml.SubElement(Style, 'Font', {'ss:Color':"#006600", 'ss:Size':"10"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Neutral", 'ss:Name':"Neutral"})
        Font = xml.SubElement(Style, 'Font', {'ss:Color':"#996600", 'ss:Size':"10"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Bad", 'ss:Name':"Bad"})
        Font = xml.SubElement(Style, 'Font', {'ss:Color':"#cc0000", 'ss:Size':"10"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Warning", 'ss:Name':"Warning"})
        Font = xml.SubElement(Style, 'Font', {'ss:Color':"#cc0000", 'ss:Size':"10"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Error", 'ss:Name':"Error"})
        Font = xml.SubElement(Style, 'Font', {'ss:Bold':"1", 'ss:Color':"#ffffff", 'ss:Size':"10"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Accent", 'ss:Name':"Accent"})
        Font = xml.SubElement(Style, 'Font', {'ss:Bold':"1", 'ss:Color':"#000000", 'ss:Size':"10"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Accent_20_1", 'ss:Name':"Accent 1"})
        Font = xml.SubElement(Style, 'Font', {'ss:Bold':"1", 'ss:Color':"#ffffff", 'ss:Size':"10"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Accent_20_2", 'ss:Name':"Accent 2"})
        Font = xml.SubElement(Style, 'Font', {'ss:Bold':"1", 'ss:Color':"#ffffff", 'ss:Size':"10"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"Accent_20_3", 'ss:Name':"Accent 3"})
        Font = xml.SubElement(Style, 'Font', {'ss:Bold':"1", 'ss:Color':"#000000", 'ss:Size':"10"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"co1"})
        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"ta1"})
        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"ce1"})
        NumberFormat = xml.SubElement(Style, 'NumberFormat', {'ss:Format':"Short Date"})

        Style = xml.SubElement(Styles, 'Style', {'ss:ID':"ce2"})
        NumberFormat = xml.SubElement(Style, 'NumberFormat', {'ss:Format':"Short Time"})

        Worksheet = xml.SubElement(root, 'ss:Worksheet', {'ss:Name':"Лист1"})
        Table = xml.SubElement(Worksheet, 'Table', {'ss:StyleID':"ta1"})

        Column = xml.SubElement(Table, 'Column', {'ss:Span':"2", 'ss:Width':"64,0063"})
        Column = xml.SubElement(Table, 'Column', {'ss:Index':"4", 'ss:Width':"64,0063"})
        Column = xml.SubElement(Table, 'Column', {'ss:Width':"64,0063"})
        Column = xml.SubElement(Table, 'Column', {'ss:Span':"3", 'ss:Width':"64,0063"})

        WorksheetOptions = xml.SubElement(ExcelWorkbook, 'x:WorksheetOptions', {})

        for i in range(0, len(data), 4):
            Row = xml.SubElement(Table, 'Row', {})

            Cell = xml.SubElement(Row, 'Cell', {})
            Data = xml.SubElement(Cell, 'Data', {"ss:Type":"String"})
            Data.text = data[i].upper()

            Cell = xml.SubElement(Row, 'Cell', {})
            Data = xml.SubElement(Cell, 'Data', {"ss:Type":"String"})
            Data.text = data[i+1].upper()

            Cell = xml.SubElement(Row, 'Cell', {})
            Data = xml.SubElement(Cell, 'Data', {"ss:Type":"String"})
            Data.text = data[i+2].upper()

            for i1 in range(0, len(data[i+3]), 6):
                Cell = xml.SubElement(Row, 'Cell', {"ss:Index":"4", "ss:StyleID":"ce1"})
                Data = xml.SubElement(Cell, 'Data', {"ss:Type":"DateTime"})
                Data.text = str(data[i+3][i1]) + 'T00:00:00.000'

                Cell = xml.SubElement(Row, 'Cell', {"ss:StyleID":"ce2"})
                Data = xml.SubElement(Cell, 'Data', {"ss:Type":"DateTime"})
                Data.text = '1899-12-31T' + str(data[i+3][i1+1])

                Cell = xml.SubElement(Row, 'Cell', {})
                Data = xml.SubElement(Cell, 'Data', {"ss:Type":"Number"})
                Data.text = str(data[i+3][i1+2])

                Cell = xml.SubElement(Row, 'Cell', {})
                Data = xml.SubElement(Cell, 'Data', {"ss:Type":"Number"})
                Data.text = str(data[i+3][i1+3])

                Cell = xml.SubElement(Row, 'Cell', {})
                Data = xml.SubElement(Cell, 'Data', {"ss:Type":"Number"})
                Data.text = str(data[i+3][i1+4])

                Cell = xml.SubElement(Row, 'Cell', {})
                Data = xml.SubElement(Cell, 'Data', {"ss:Type":"Number"})
                Data.text = str(data[i+3][i1+5])

                if (i1 < (len(data[i+3])-1)):
                    Row = xml.SubElement(Table, 'Row', {})

        tree.write(FileName, "utf-8", True)
