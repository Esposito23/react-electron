# sensore di misura di pressione relativa
# indirizzo RevPi sensore di pressione: (modulo AI0_2 - pin I_1)
# impostare lettura in tensione da PiCtory sul pin interessato

import revpimodio2
import threading

active = False
hist = []

IN_MAX = 10000
IN_MIN = 0
OUT_MAX = 10
OUT_MIN = 1

def init(RPI):
    global rpi
    rpi= RPI

def monitor():
    global active
    volt_sensor = rpi.io.InputValue_1.value
    bar = volt2bar(volt_sensor)
    hist.append(bar)
    if len(hist) > 10:
        del hist[0]
    if active:
        threading.Timer(1.0,monitor).start()

def volt2bar(x):
    return (x - IN_MIN) * (OUT_MAX - OUT_MIN) / (IN_MAX - IN_MIN) + OUT_MIN

def average():
    global active
    if active:
        m = sum(hist) / len(hist)
        print (m)

def last():
    global active
    if len(hist) > 0 and monitor:
        print(hist[-1])

def monitor_on():
    global active
    if not active:
        active = True
        monitor()

def monitor_off():
    global active
    active = False

def close():
    monitor_off()
 