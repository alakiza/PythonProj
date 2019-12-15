# This Python file uses the following encoding: utf-8
from PyQt5 import QtWidgets
import sys
import serial
import time
import struct

class SerialDevice:
    def __init__(self, port, speed):
        self.__port  = port
        self.__speed = speed

    #return list [temperature, Pulse, systolic, diastolic]
    def Run(self):
        try:
            SerialConnection = serial.Serial(self.__port, self.__speed)

            time.sleep(2)
            print(SerialConnection.port)
            print(SerialConnection.baudrate)
            print(bytes([0x0F, 0xAF, 0xCF, 0xFF]))
            SerialConnection.reset_input_buffer()
            SerialConnection.timeout = 20
            SerialConnection.write(bytes([0x0F, 0xAF, 0xCF, 0xFF]))

            ReplyBytes = SerialConnection.read(4)
            print(ReplyBytes)
            if len(ReplyBytes) == 4:
                if((ReplyBytes[0] == 0xF0) and
                   (ReplyBytes[1] == 0x40) and
                   (ReplyBytes[2] == 0x20) and
                   (ReplyBytes[3] == 0x00)
                   ):
                    SerialConnection.timeout = 120

                    PackedBytes = SerialConnection.read(16)
                    print(PackedBytes)
                    res = []
                    res.append(struct.unpack('<f', PackedBytes[0:4])[0])
                    res.append(struct.unpack('<f', PackedBytes[4:8])[0])
                    res.append(struct.unpack('<f', PackedBytes[8:12])[0])
                    res.append(struct.unpack('<f', PackedBytes[12:16])[0])

                    return res
            raise Exception("Нет устройства")
        except (OSError, serial.SerialException):
            print('Error while using Serial')
        finally:
            SerialConnection.close()
