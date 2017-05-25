import os
import sys
import serial

putvalue = ""

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        putvalue += sys.argv[i] + " "
    
    putvalue = putvalue[:-1]

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

#PUT VALUE TO ARDUINO
if serial_conn.is_open:
    serial_conn.write(putvalue.encode("utf-8"))

    serial_conn.close()

    sys.stdout.write("OK")

else:
    sys.stdout.write("NOT")