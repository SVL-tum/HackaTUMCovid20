from datetime import date, time

from flask import Flask, request
import json
from time import sleep
import requests
from Hackathon import Patient
from Hackathon import VentilatorOld as Ventilator
from collections import OrderedDict


app = Flask(__name__)

x = dir(Patient)
print(x)
x = dir(Ventilator)
print(x)

patients = Patient.get_patients()

## get ventilators
ventilator_ids = [4242, 3089, 12693, 93, 586]
ventilators = []

for venid in ventilator_ids:
    v = Ventilator.Ventilator(venid)
    ventilators.append(v)

for i in range(10):
    sleep(0.5)
    r = requests.get('https://api.theopenvent.com/exampledata/v2/data', verify=False)
    data = r.json()
    for key in data:
        for v in ventilators:
            if data[key]['device_id'] == v.id:
                v.add_data(data[key])



map_patients_to_ventilator = OrderedDict()
map_ventilators_to_patients = OrderedDict()
for idx, p in enumerate(patients):
    map_patients_to_ventilator[p] = ventilators[idx]
    map_ventilators_to_patients[ventilators[idx]] = p


counter = 0

@app.route('/patient')
def get_patient_list():
    sorting = request.args.get('sorting')
    global patients
    global map_patients
    global serialize
    for p in map_patients_to_ventilator:
        p.set_severity(map_patients_to_ventilator[p].severity_score())

    if sorting == 'rscore':
        patients_new = sorted(patients, key=lambda patient: patient.rscore, reverse=True)
    elif sorting == 'severity':
        patients_new = sorted(patients, key=lambda patient: patient.severity, reverse=True)
    elif sorting == 'age':
        patients_new = sorted(patients, key=lambda patient: patient.age, reverse=True)

    patients = json.dumps(patients_new, default=lambda o: o.__dict__)
    return patients

   # user = request.args.get('name')

   #
    #return patients

@app.route('/data')
def data():
    return 'Very important data'

# Does not execute this
if __name__ == '__main__':
    print("hi")
    app.run(host='0.0.0.0')

