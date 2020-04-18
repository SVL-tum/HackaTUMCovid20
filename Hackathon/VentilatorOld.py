from collections import OrderedDict
from time import sleep
from typing import Dict
import random

import requests


class Ventilator:
    def __init__(self, id):
        self.id: str = id
        self.data = OrderedDict()

    def add_data(self, json):
        self.data[json['time']] = json

    def severity_score(self):
        # Get the most recent entry of the ventilator data
        if len(self.data) > 0:
            last_entry = self.data[next(reversed(self.data))]

        # Calculate patient serverity
        # Content docs:

        return random.randint(0, 2)
        #return len(self.data)

    def get_last_seconds(self, number_of_sec):
        iter = reversed(self.data)
        results = []
        for i in range(min(number_of_sec, len(self.data))):
            results.append(self.data[next(iter)])

        results.reverse()
        return  results



if __name__ == "__main__":
        v = Ventilator(4242)
        for i in range(10):
            sleep(0.5)
            r = requests.get('http://api.theopenvent.com/exampledata/v2/data', verify=False)
            data = r.json()

            for key in data:
                if data[key]['device_id'] == v.id:
                    v.add_data(data[key])

        test = v.get_last_seconds(4)
        print(test)