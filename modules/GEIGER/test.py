import sys
import os

getValue = os.popen("python3 " + os.path.dirname(os.path.abspath(__file__)) + "/get.py").read()

if float(getValue) != None:
    sys.stdout.write("OK")
else:
    sys.stdout.write("NOT")