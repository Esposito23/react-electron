import time
from flask import Flask

from digi.xbee.devices import XBeeDevice


app = Flask(__name__)



@app.route('/comando')
def comando():
    print('Comando inoltrato',flush=True)
    return {'m': "Comando inoltrato"}


# if __name__ == "__main__":
#     app.run(debug = True, host='192.168.1.129',Port=80)
