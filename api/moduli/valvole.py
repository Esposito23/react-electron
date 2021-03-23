# CONTROLLO ELETTROVALVOLE E POMPE LIQUIDI/GAS
#
# si segue lo schema circuiti fluidici v2.0
#
# L = liquidi, G = gas
# 1x Pompa per Gas (X-SVCO-SP622 EC-BL-DU-HR-DV)
# 1x Pompa per Liquidi (X-SVCO-SP725 EC-TH-L (DC))
# 10x "Elettrovalvole 2/2 vie ( 0330-A-03,0-FF-MS-GM82-024/DC-08JH54)"
# 1x Elettrovalvole 3/2 vie ( 0330-C-03,0-FF-MS-GM82-024/DC-08)
#
#  controllo tramite modulo DIO
#
# ----- INLET/OUTLET - liquidi -----
# L1 <---> O_1
# L2 <---> O_2
# L3 <---> O_3
# RL1 <---> O_4
# L_out <---> O_5
#
# ----- INLET - gas -----
# G1 <---> O_6
# G2 <---> O_7
# G3_out (3 VIE) <---> O_8
#
# ----- Vacuum + OUTLET - gas -----
# RG1 <---> O_9
# InAir_waste <---> O_10
# RG_out <---> O_11
#
# ----- Pompe -----
# da definire <--->

import revpimodio2


def init(RPI):
    global rpi
    global valveState
    rpi=RPI
    valveState={}
    valveState["L1"] = ["O_1",0]
    valveState["L2"] = ["O_2",0]
    valveState["L3"] = ["O_3",0]
    valveState["RL1"] = ["O_4",0]
    valveState["L_out"] = ["O_5",0]
    valveState["G1"] = ["O_6",0]
    valveState["G2"] = ["O_7",0]
    valveState["G3_out"] = ["O_8",0]
    valveState["RG1"] = ["O_9",0]
    valveState["InAir_waste"] = ["O_10",0]
    valveState["RG_out"] = ["O_11",0]


def change_state(name, new_state):
    valveState[name][1] = new_state
    pin = valveState[name][0]
    rpi.io[pin].value = int(new_state)


def set_state(name, new_state):
    if name in valveState:
        if new_state == '0' or new_state == '1':
            change_state(name, new_state)
            return(name,new_state)
        else:
            return('Valore non consentito')
    else:
        return('Valvola non presente')

def get_valves_state(name):
        return(valveState[name][1])

def get_state():
    state= {name: valveState[name][1] for name in valveState.keys()}
    return(str(state))

def close():
    for valv in valveState.keys():
        rpi.io[valveState[valv][0]].value = 0
