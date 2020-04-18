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



if __name__ == "__main__":
    for venid in list:
        v = Ventilator(venid)
        for i in range(10):
            sleep(0.5)
            r = requests.get('http://api.theopenvent.com/exampledata/v2/data')
            data = r.json()

            for key in data:
                if data[key]['device_id'] == v.id:
                    v.add_data(data[key])

        v.severity_score()