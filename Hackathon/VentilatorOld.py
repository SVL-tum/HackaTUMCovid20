import copy
from collections import OrderedDict
from time import sleep
import numpy as np
from typing import Dict
import random

import requests

def mock(value, timestamp):
    return value*(np.sin(int(timestamp)*0.3) + 3) * 0.5

class Ventilator:
    def __init__(self, id):
        self.id = id
        self.data = OrderedDict()
        self.counter = 0

    def add_data(self, json):
        self.data[json['time']] = json

    # son = copy.deepcopy(json_s)
    # if self.id == 4242:
    #     a = (np.sin(self.counter) + 3) * 0.5
    #     json['processed']['ExpiredO2'] = json['processed']['ExpiredO2'] * a
    #     self.counter += 0.1


    def severity_score(self):
        # Get the most recent entry of the ventilator data
        if len(self.data) > 0:
            last_entry = self.data[next(reversed(self.data))]
            last_timestamp = next(reversed(self.data))
            MVe = int(last_entry['processed']['MVe'])
            ExpiredCO2 = int(last_entry['processed']['ExpiredCO2'])
            ExpiredO2 = int(last_entry['processed']['ExpiredO2'])
            if self.id == 4242:
                ExpiredO2 = mock(ExpiredO2 , last_timestamp)
            frequency = int(last_entry['processed']['frequency'])
            # pressure = last_entry['processed']['pressure']

            criticalList = []

            if MVe > 10000:
                a = 1
            elif MVe < 1500:
                a = 3
            #    criticalList.append('MVe')
            elif MVe < 4000:
                a = 1
            else:
                a = 0

            if ExpiredCO2 < 3.5:
                b = 1
            elif ExpiredCO2 > 6:
                b = 3
                criticalList.append('Expired CO2')
            elif ExpiredCO2 > 4.5:
                b = 1
            else:
                b = 0

            print(ExpiredO2)
            if ExpiredO2 < 16:
                c = 5
            elif ExpiredO2 > 50:
                c = 5
            else:
                c = 2

            if frequency < 10:
                d = 3
            elif frequency < 13:
                d = 1
            elif frequency > 23:
                d = 3
                criticalList.append('Frequency')
            elif frequency > 20:
                d = 1
            else:
                d = 0

                # FiO2 = last_entry['processed']['triggerSettings'] ['FiO2']
            # IE = last_entry['processed']['triggerSettings'] ['IE']
            PEEP = int(last_entry['processed']['triggerSettings']['PEEP'])
            RR = int(last_entry['processed']['triggerSettings']['RR'])
            VT = int(last_entry['processed']['triggerSettings']['VT'])
            pressure_max = int(last_entry['processed']['triggerSettings']['pressure_max'])
            # volumePerMinute = last_entry['processed'] ['ventilationMode'] ['volumePerMinute']

            if PEEP < 5:
                e = 1
            elif PEEP > 18:
                e = 1
            else:
                e = 0

            if RR < 16:
                f = 1
            elif RR > 20:
                f = 1
            else:
                f = 0

            if VT < 300:
                g = 1
            elif VT > 600:
                g = 1
            else:
                g = 0

            if pressure_max < 20:
                h = 1
            elif pressure_max > 30:
                h = 1
            else:
                h = 0

            score_total = a + b + c + d + e + f + g + h
            if score_total <= 4:
                score = 0
            elif score_total <= 8:
                score = 1
            else:
                score = 2

        return [score, criticalList]


        #return random.randint(0, 2)
        #return len(self.data)

    def get_last_seconds(self, number_of_sec):
        iter = reversed(self.data)
        results = []
        for i in range(min(number_of_sec, len(self.data))):
            results.append(self.data[next(iter)])

        results.reverse()
        return results


ventilator_ids = [4242, 3089, 12693, 93, 586]

if __name__ == "__main__":
        v = Ventilator(1000)
        for i in range(1):
            sleep(0.5)
            r = requests.get('http://api.theopenvent.com/exampledata/v2/data', verify=False)
            data = r.json()

            for key in data:
                if data[key]['device_id'] == v.id:
                    v.add_data(data[key])

        test = v.severity_score()
        print(test)

