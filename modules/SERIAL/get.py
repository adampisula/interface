import os
import sys
import serial

#JUST IN CASE YOU'LL NEED TO CHECK OUTPUT
def pletters(text):
    ret = ""

    for i in range(0, len(text)):
        ret += "[" + str(ord(text[i])) + "] "

    return ret

#NEW CONNECTION
serial_conn = serial.Serial()
serial_conn.baudrate = 9600

ports = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2']

#CONNECT TO FREE PORT
for i in range(0, len(ports)):
    if os.path.exists(ports[i]):
        serial_conn.port = ports[i]

        break

serial_conn.open()

getline = ""

#GET VALUE FROM ARDUINO
if serial_conn.is_open:
    while (getline == "") or (getline == "\n"):
        getline = serial_conn.read(32).decode("utf-8").split("\r\n")[1]

    serial_conn.close()

    sys.stdout.write(getline)