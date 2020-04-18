from collections import OrderedDict
from time import sleep
from typing import Dict

import requests


class Ventilator:
    def __init__(self, id):
        self.id: str = id
        self.data = None

    def add_data(self, json):
        self.data = json

    def severity_score(self):
        last_entry = self.data
        MVe = last_entry['processed']['MVe']
        ExpiredCO2 = last_entry['processed'] ['ExpiredCO2']
        ExpiredO2 =  last_entry['processed'] ['ExpiredO2']
        frequency = last_entry['processed']['frequency']
        #pressure = last_entry['processed']['pressure']
        
        changeInFrequency = np.zeros_like(time)

        for n in time [:-5]:
            changeInFrequency[i+5] = (frequency[n+5]/frequency[n+4]
            + frequency[n+4]/frequency[n+3] + frequency[n+4]/frequency[n+2]
            + frequency[n+2]/frequency[n+1] + frequency[n+1]/frequency[n] ) /5
            i=i+1
            
        if MVe > 10 :
            a = 1
        elif MVe < 3:
            a = 3
        elif MVe < 5:
            a = 1
        else: 
            a = 0
            
        if ExpiredCO2 < 3.5 :
            b = 1
        elif ExpiredCO2 > 5.5:
            b = 3
        elif ExpiredCO2 > 4.5:
            b = 1
        else: 
            b = 0
           
        if ExpiredO2 > 19 :
            c = 1
        elif ExpiredO2 > 12:
            c = 3
        elif ExpiredO2 > 14:
            c = 1
        else: 
            c = 0   
            
        if frequency < 10 :
            d = 3
        elif frequency < 13:
            d = 1
        elif frequency > 23:
            d = 3
        elif frequency > 20:
            d = 1
        else: 
            d = 0  
            
         
             
        #FiO2 = last_entry['processed']['triggerSettings'] ['FiO2']
        #IE = last_entry['processed']['triggerSettings'] ['IE']
        PEEP = last_entry['processed']['triggerSettings'] ['PEEP']
        RR = last_entry['processed']['triggerSettings'] ['RR']
        VT = last_entry['processed']['triggerSettings'] ['VT']
        pressure_max = last_entry['processed']['triggerSettings'] ['pressure_max']
        #volumePerMinute = last_entry['processed'] ['ventilationMode'] ['volumePerMinute']

        if PEEP < 5 :
            e = 1
        elif PEEP > 18:
            e = 1
        else: 
            e = 0  
            
        if RR < 16 :
            f = 1
        elif RR > 20:
            f = 1
        else: 
            f = 0  
        
        if VT < 4 :
            g = 1
        elif VT > 8:
            g = 1
        else: 
            g = 0 
            
        if pressure_max < 20 :
            h = 1
        elif pressure_max > 30:
            h = 1
        else: 
            h = 0 

        
        score_total = a+b+c+d+e+f+g+h
        if score_total <= 4:
            score = 0
        elif score_total <= 8:
            score = 1
        else:
            score = 2
                
        return score


def get_ventilators():
    ventilator_list = []
    for i in range(8):
        ventilator_list.append(Ventilator(4242))
    return ventilator_list

if __name__ == "__main__":
    v = Ventilator(4242)
    r = requests.get('http://api.theopenvent.com/exampledata/v2/data', verify=False)
    data = r.json()

    for key in data:
        if data[key]['device_id'] == v.id:
            v.add_data(data[key])

    v.severity_score()

