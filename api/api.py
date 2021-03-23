import time
from flask import Flask, request, jsonify, after_this_request
from tools import port
from digi.xbee.devices import XBeeDevice
import revpimodio2
from moduli import rotante , lineare, digixbeeusb,pressione,lpump, valvole


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

# Motore Lineare
# ---------------------------------------------------------------
@app.route('/linearHome')
def linearHome():
    lineare.home()
    return jsonify({'stato' : 'Il motore si sta muovendo in Home'})

@app.route('/linearAway')
def linearAway():
    lineare.away()
    return jsonify({'stato' : 'Il motore si sta muovendo in Away'})

@app.route('/linearStop')
def linearStop():
    lineare.stop()
    return jsonify({'stato' : 'Motore Bloccato Manualmente'})

# ---------------------------------------------------------------

# Digi<--> Xbee  (mancano i comandi di set ecc)
# ---------------------------------------------------------------
@app.route('/xbeeLast')
def lastXbee():
    last=digixbeeusb.last()
    return jsonify({'last' : last})

@app.route('/xbeeCheck')
def checkXbee():
    digixbeeusb.check()
    return jsonify({'info' : 'Inviato processo di check connessione'})

@app.route('/xbeeReset')
def resetXbee():
    digixbeeusb.reset()
    return jsonify({'info' : 'Reset Xbee, attendi qualche secondo'})
# ---------------------------------------------------------------


# Sensore di pressione
# ---------------------------------------------------------------
@app.route('/pressOff')
def pressOff():
    pressione.monitor_off()
    return jsonify({'monitor' : 'Monitoraggio pressione bloccato'})

@app.route('/pressOn')
def pressOn():
    pressione.monitor_on()
    return jsonify({'monitor' : 'Monitoraggio pressione iniziato'})

@app.route('/pressLast')
def pressLast():
    pressione.last()
    return jsonify({'monitor' : 'Richiesta ultima lettura'})

@app.route('/pressAvg')
def pressAvg():
    pressione.average()
    return jsonify({'monitor' : 'Richiesta ultima media di pressione'})


# ---------------------------------------------------------------


# Lpump
# ---------------------------------------------------------------
@app.route('/lPumpOff')
def lpumpOff():
    lpump.pumpOff()
    return jsonify({'state' : 'Pompa spenta'})

@app.route('/lPumpOn')
def lpumpOn():
    lpump.pumpOn()
    return jsonify({'state' : 'Pompa Accesa'})

@app.route('/lPumpSec')
def lpumpSec():
    lpump.attiva(float(20))
    return jsonify({'state' : 'Erogazione di 20 ml'})

# ---------------------------------------------------------------

# Valvole
# ---------------------------------------------------------------
@app.route('/valvState')
def valvState():
    state=valvole.get_state()
    return jsonify({'state' : state})

@app.route('/valvGet')
def valvGet():
    valv= valvole.get_valves_state("L1")
    return jsonify({'state' : valv})

@app.route('/valvSet')
def valvSet():
    setValv = valvole.set_state('L1','1')
    return jsonify({'state', setValv})

    
# ---------------------------------------------------------------


device=init_digi()
rpi = revpimodio2.RevPiModIO(autorefresh=True)
rpi.mainloop(blocking=False)
digixbeeusb.init(device)
pressione.init(rpi)
rotante.init(rpi)
lineare.init(rpi)
lpump.init(rpi)
valvole.init(rpi)



