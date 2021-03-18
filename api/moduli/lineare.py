import revpimodio2

def init(RPI):
	print('Init')
	global rpi
	rpi= RPI
    
def finecorsaA(ioname,iovalue):
	print("Input %s has value %d" % (ioname,iovalue))
	rpi.io.O_5.value = 0 # stop motorA

def finecorsaB(ioname,iovalue):
	print("Input %s has value %d" % (ioname,iovalue))
	rpi.io.O_7.value = 0 # stop motorB

def home():
	rpi.io.O_4.value = 0 # set directionA
	rpi.io.O_5.value = 1 # start motorA
	rpi.io.O_6.value = 0 # set directionB
	rpi.io.O_7.value = 1 # start motorB

def away():
	rpi.io.O_6.value = 1 # set directionB
	rpi.io.O_7.value = 1 # start motorB
	rpi.io.O_4.value = 1 # set directionA
	rpi.io.O_5.value = 1 # start motorA

def stop():
    rpi.io.O_5.value = 0 # stop motorA
    rpi.io.O_7.value = 0 # stop motorB

