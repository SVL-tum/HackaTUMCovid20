# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

# HackaTUM Infineon Projekt
import numpy as np
import matplotlib.pyplot as plt
import json



# 1.Data Mining [json]


#1.1 Load Json Data

#data = json.loads('data.json')
# converts object into dict, array into list, null into none ...
# for key in data[mockup_data]:
#    print(key['time'])

#1.2 Define Element class of Ventilator (vent)

class VentOne:
    time = 0
    volumePerMovement = 0
    frequency = 0
    volumePerMinute = 0
    ventilationMode = 'A'
    O2 = 0
    CO2 = 0
    humidity = 0
    pressure = 0
    pressure_mean = 0
    mve = 0
    RR = 0
    VT = 0
    PEEP = 0
    pressure1 = 0
    pressure2 = 0
    temperature1 = 0
    temperature2 = 0
    rawCO2 = 0
    rawO2 = 0
    angleSensor = 0
    current = 0
    motorRPM = 0
    
    def __init__(self, time = 0,
    volumePerMovement = 0,
    frequency = 0,
    volumePerMinute = 0,
    ventilationMode = 'A',
    O2 = 0,
    CO2 = 0,
    humidity = 0,
    pressure = 0,
    pressure_mean = 0,
    mve = 0,
    RR = 0,
    VT = 0,
    PEEP = 0,
    pressure1 = 0,
    pressure2 = 0,
    temperature1 = 0,
    temperature2 = 0,
    rawCO2 = 0,
    rawO2 = 0,
    angleSensor = 0,
    current = 0,
    motorRPM = 0):
        self.time = time 
        self.volumePerMovement = volumePerMovement
        self.frequency = frequency
        self.volumePerMinute = volumePerMinute 
        self.ventilationMode = ventilationMode
        self.O2 = O2
        self.CO2 = CO2
        self.humidity = humidity
        self.pressure = pressure
        self.pressure_mean = pressure_mean
        self.mve = mve
        self.RR = RR
        self.VT = VT
        self.PEEP = PEEP
        self.pressure1 = pressure1
        self.pressure2 = pressure2
        self.temperature1 = temperature1
        self.temperature2 = temperature2
        self.rawCO2 = rawCO2
        self.rawO2 = rawO2
        self.angleSensor = angleSensor
        self.current = current
        self.motorRPM = motorRPM
        
    def printvent(self):
        print('PEEP: ', self.PEEP)
        
test_vent = VentOne (0,0,0,0,'A',0,0,0,0,1,0,1,1,0,0,10,2,2,3,4,5,6,7)
test_vent.printvent()
        
        
#1.3 Define Element class of Patient (PatOne)
    
class PatOne(VentOne):
    name = 'Egon'
    age = 4
    smoker = True
    bmi = 20
    rscore = 5
   

    def __init__(self, name = 'Egon', age=4, smoker=True, bmi=20, rscore=5, time = 0,
        volumePerMovement = 0,
        frequency = 0,
        volumePerMinute = 0,
        ventilationMode = 'A',
        O2 = 0,
        CO2 = 0,
        humidity = 0,
        pressure = 0,
        pressure_mean = 0,
        mve = 0,
        RR = 0,
        VT = 0,
        PEEP = 0,
        pressure1 = 0,
        pressure2 = 0,
        temperature1 = 0,
        temperature2 = 0,
        rawCO2 = 0,
        rawO2 = 0,
        angleSensor = 0,
        current = 0,
        motorRPM = 0):
        super(PatOne, self).__init__(time = 0,
    volumePerMovement = 0,
    frequency = 0,
    volumePerMinute = 0,
    ventilationMode = 'A',
    O2 = 0,
    CO2 = 0,
    humidity = 0,
    pressure = 0,
    pressure_mean = 0,
    mve = 0,
    RR = 0,
    VT = 0,
    PEEP = 0,
    pressure1 = 0,
    pressure2 = 0,
    temperature1 = 0,
    temperature2 = 0,
    rawCO2 = 0,
    rawO2 = 0,
    angleSensor = 0,
    current = 0,
    motorRPM = 0)
        self.name = name
        self.age = age
        self.smoker = smoker
        self.bmi = bmi
        self.rscore = rscore
        
    
    def printpat(self):
        print('name: ', self.name)
        print('smoker: ', self.smoker)

test_pat = PatOne('Bonny', 7, False, 30, 4)
test_pat.printpat()   
test_pat.printvent() 

# 2.Data Cleaning [numpy, pandas]

# 3.Data Exploration (Correlationen, Feature Definition, Plots) [matplotlib, pandas]

# 4.Data Transfer (to App and Server)
# transfer ID and Stuatus

# 5. Optional: Add data input from App about anamnesis



### Notes: Clearing when patient changes!
###        Add Password safety
###        Sorting mechanism
###        Bauch-/Rückenlagerung (max. 16 Bauch, 4 Stunden Rücken)