import serial
import time
import Methods

#TODO: Ask poorna why i cant do string operations within method
#get this working with string manipulation and then work with integers

#start script
ser = serial.Serial('COM4', 9600, timeout = 2)
ser.send_break()

#The Startup Routine
output = bytes('', 'utf-8')
time.sleep(2)
while ser.in_waiting:
    output = ser.readline()
    output = output.decode('utf-8')
    output = output.rstrip()
    if output == '' or output.isdigit():
        continue
    elif output == '>':
        ser.flushOutput()
        key = 1
        break
    else:
        print(output)

#begin polling
dataEnsemble = bytes('', 'utf-8')
while 1:
    while ser.in_waiting:
        dataEnsemble = ser.readline()
        dataEnsemble = dataEnsemble.decode('utf-8')
        dataEnsemble = dataEnsemble.rstrip()
        if dataEnsemble != '':
            print('>>', dataEnsemble + '\r\n')
            Methods.Print_Velocity_Information(dataEnsemble)