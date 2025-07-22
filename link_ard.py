import serial.tools.list_ports
from soun_vosk import Sound

#import all the ports to save it in a list
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
# The list that we will save in it the info of (ports)
portsLists = []
sound = Sound()

for one in ports:

    portsLists.append(str(one))
    print(str(one))

com = input("Choose a port for the Arduio #: ")

# Check if the port is valid
for i in range(len(portsLists)):

    if portsLists[i].startswith("/dev/ttyACM" + str(com)):

        use = "/dev/ttyACM" + str(com)
        print(use)

serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()

while True:

    sound_result = sound.Open()
    print(sound_result)
    serialInst.write(sound_result.encode('utf-8'))

    if sound_result == 'exit':
        exit()