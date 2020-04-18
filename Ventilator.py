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
        trigger_setting_for_Fio2 = last_entry['processed']['triggerSettings']['FiO2']
        print(f'trigger Setting for FIO2= {trigger_setting_for_Fio2}')

        # Calculate patient serverity
        # Content docs: http://api.theopenvent.com/exampledata/v2/doku

        #TODO
        print("Debug here")
        return 1


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

