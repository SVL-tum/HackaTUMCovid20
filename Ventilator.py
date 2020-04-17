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

        # Calculate patient serverity
        # Content docs: http://api.theopenvent.com/exampledata/v2/doku

        #TODO
        print("Debug here")
        pass


if __name__ == "__main__":
    v = Ventilator(4242)
    r = requests.get('http://api.theopenvent.com/exampledata/v2/data')
    data = r.json()

    for key in data:
        if data[key]['device_id'] == v.id:
            v.add_data(data[key])

    v.severity_score()

