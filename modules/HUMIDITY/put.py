import sys

if len(sys.argv) > 1:
    inArgs = ""

    for inc in range(2, len(sys.argv)):
        inArgs += sys.argv[inc] + " "

    sys.stdout.write("Input: " + inArgs)
    
else:
    sys.stdout.write("NO INPUT")