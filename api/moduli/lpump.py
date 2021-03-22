# Test di gestione della pompa per liquidi
# Mod. SP725 EC-TH-L (DC), 24V 7s54073
# 850mA MAX
# parallel only
# 1400 ml/min ===> 23,33 ml/sec
# pressione max: 10 mH20 (metro colonna d'acqua, eq. a 10*9806,65 Pa)

# indirizzo RevPi pompa liquidi: (modulo DI0_0 - pin O_3)

import revpimodio2
import threading

portata = 23.33 #ml/sec

def init(RPI):
    global rpi
    rpi= RPI
    pumpOff()


def attiva(ml):
    if rpi.io.O_3.value:
        print('Pompa gia attiva, attendere fine processo o forzare chiusura')
    else:
        sec = float(ml/portata)
        pumpOn()
        threading.Timer(sec,pumpOff).start()

def pumpOn():
    rpi.io.O_3.value = 1 #pump on

def pumpOff():
    rpi.io.O_3.value = 0 #pump off