from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.devices import XBee64BitAddress
import struct
from time import time
 
last_sign= time()

def init(dev):
    global device
    global remote_device
    device = dev
    #remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041909AFC")) #OnePotA
    remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041AEF25C")) #prototipo
    device.add_data_received_callback(callback)
    
def reset():
    global last_sign
    last_sign = time()
    remote_device.reset()

def last():
    global last_sign
    return ('%.1f' %(time() - last_sign))


def callback(xbee_message):
    global last_sign
    last_sign = time()
    data = xbee_message.data
    if len(data)==32:
        convert = struct.unpack('8f', data)
        print(convert)
    else:
        print(data.decode('utf-8'))

def check():
    device.send_data(remote_device,'check')

def send_cmd(command):
    global last_sign
    last_sign = time()
    device.send_data(remote_device,command)