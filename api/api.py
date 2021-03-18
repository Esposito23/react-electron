import time
from flask import Flask, request, jsonify
from tools import port
from digi.xbee.devices import XBeeDevice
import revpimodio2
from moduli import rotante


app = Flask(__name__)


def init_digi():
    device = XBeeDevice(port(), 9600)
    device.open()
    return(device)


# Motore rotante
# ---------------------------------------------------------------
@app.route('/motorOn')
def motorOn():
    rotante.start_motor(12)
    return jsonify({'stato':'motore acceso'})

@app.route('/motorOff')
def motorOff():
    rotante.stop_motor()
    return jsonify({'stato':'motore spento'})

@app.route('/monitorOn')
def monitorOn():
    rotante.monitor_on()
    return jsonify({'monitor': 'Monitor Acceso'})

@app.route('/monitorOff')
def monitorOff():
    rotante.monitor_off()
    return jsonify({'monitor': 'Monitor Spento'})

@app.route('/monitorLast')
def speedLast():
    last=rotante.last()
    return jsonify({'speed': 'Ultima lettura di velocità instantanea : '+str(last) })

@app.route('/monitorMean')
def speedMean():
    mean=rotante.average()
    return jsonify({'speed':'Ultima lettura di velocità media : '+ str(mean)})

# ---------------------------------------------------------------

# device=init_digi()
rpi = revpimodio2.RevPiModIO(autorefresh=True)
rpi.mainloop(blocking=False)
rotante.init(rpi)



