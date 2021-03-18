import revpimodio2
import threading
active = False
hist = []


def init(RPI):
    global rpi
    rpi= RPI
    rpi.io.PWM_2.value = 0
    rpi.io.Counter_9.reset()

def start_motor(duty):
    rpi.io.PWM_2.value = duty

def stop_motor():
    rpi.io.PWM_2.value = 0

def monitor():
    global active
    freq = rpi.io.Counter_9.value
    rpi.io.Counter_9.reset()
    hist.append(freq)
    if len(hist) > 10:
        del hist[0]
    if active:
        threading.Timer(1.0,monitor).start()

def last():
    global active
    if len(hist) > 0 and monitor:
        return (hist[-1] * 60.0 / 36.0)
    else:
        return -1

def monitor_on():
    global active
    if not active:
        active = True
        monitor()

def monitor_off():
    global active
    active = False

def average():
    global active
    if active:
        m = sum(hist) / len(hist)
        return m * 60.0 / 36.0
    else:
        return -1

def close():
    monitor_off()
    stop_motor()


