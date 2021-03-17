import revpimodio2


def init(RPI):
    global rpi
    rpi= RPI
    rpi.io.PWM_2.value = 0
    rpi.io.Counter_9.reset()

def start_motor(duty):
    rpi.io.PWM_2.value = duty

def stop_motor():
    rpi.io.PWM_2.value = 0



