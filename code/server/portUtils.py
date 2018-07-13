# PortUtils
# A simple helper class to get the data from serial port until a CR LF
#
# MIT License
# Copyright (c) 2018 Prototyping Corner
# prototypingcorner.io


import os
import serial

# A simple class helper class for serial
class PortUtils():
    def __init__(self, port, baud):
        self.__serialPort = serial.Serial(port, baud)

    # Read data from the port until a CRLF
    def read(self):
        buffer = ''
        CRLF = '\r\n' # Carriage Return Line Feed
        while True:
            buffer += self.__serialPort.read()
            if CRLF in buffer:
                buffer = buffer.split(CRLF)
                return buffer[0]

    # Write data to the serial port
    def write(self, data):
        self.__serialPort.write(data)

if __name__ == "__main__":
    print "Woops. You need to run me from a python script!"
