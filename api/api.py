import time
from flask import Flask, request, jsonify
from tools import port
from digi.xbee.devices import XBeeDevice
import revpimodio2
from motor import start_motor,init,stop_motor


app = Flask(__name__)


def init_digi():
    device = XBeeDevice(port(), 9600)
    device.open()
    return(device)



@app.route('/motorOn')
def motorOn():
    start_motor(15)
    return jsonify({'m':'motore acceso'})

@app.route('/motorOff')
def motorOff():
    stop_motor()
    return jsonify({'m':'motore spento'})


# device=init_digi()
rpi = revpimodio2.RevPiModIO(autorefresh=True)
rpi.mainloop(blocking=False)
init(rpi)



