import serial.tools.list_ports

def port():
    ports = serial.tools.list_ports.comports()
    for port, _ , hwid in ports:
        if 'ttyUSB' in port and hwid.split()[-1] == "LOCATION=1-1.3":   #set this port LOCATION=1-1.P , P=(1,2,3,4)
            return(port)