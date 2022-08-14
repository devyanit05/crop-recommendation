import esptool
import serial.tools.list_ports
#from serial.tools import list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select port: COM")

print(val)

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

def n_value():
    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            op = print(packet.decode('utf').rstrip('\n'))
            return op
# serialInst.close()

