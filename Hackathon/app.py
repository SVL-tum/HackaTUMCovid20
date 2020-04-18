import sys
from datetime import date, time

from flask import Flask, request
import json
from time import sleep
import requests
from Hackathon import Patient
from Hackathon import VentilatorOld as Ventilator
from collections import OrderedDict
from _thread import start_new_thread

#link to communicate externally: http://129.187.212.1:5000/patient?sorting=rscore
#Link to communicate internally: curl localhost:5001/data?"patientid=1000&seconds=300&measurement=O2"

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
#
# for i in range(10):
#     sleep(0.5)
#     r = requests.get('https://api.theopenvent.com/exampledata/v2/data', verify=False)
#     data = r.json()
#     for key in data:
#         for v in ventilators:
#             if data[key]['device_id'] == v.id:
#                 v.add_data(data[key])

def continous_update_of_ventilators():
    while 1==1:
      sleep(0.5)
      r = requests.get('https://api.theopenvent.com/exampledata/v2/data', verify=False)
      data = r.json()
      for key in data:
         for v in ventilators:
            if data[key]['device_id'] == v.id:
                    v.add_data(data[key])

start_new_thread(continous_update_of_ventilators, ())


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
    patients_new = patients
    if sorting == 'rscore':
        patients_new = sorted(patients, key=lambda patient: patient.rscore, reverse=True)
    elif sorting == 'severity':
        patients_new = sorted(patients, key=lambda patient: patient.severity, reverse=True)
    elif sorting == 'age':
        patients_new = sorted(patients, key=lambda patient: patient.age, reverse=True)

    return json.dumps(patients_new, default=lambda o: o.__dict__)

   # user = request.args.get('name')

   #
    #return patients

@app.route('/tdata')
def get_tventilator_data():
    global ventilators
    ventilator_for_chris = []
    patientid = int(request.args.get('patientid'))
    measurement = request.args.get('measurement')
    seconds = int(request.args.get('seconds'))
    print(patientid, measurement, seconds)
    all_about_ventilator = None
    for p in map_patients_to_ventilator:
        if p.id == patientid:
            all_about_ventilator = map_patients_to_ventilator[p].get_last_seconds(seconds)
    if all_about_ventilator is None:
        return "Patient "+str(patientid)+" not found"
    timestamps = []
    for timepoints in all_about_ventilator:
        timestamps.append(timepoints['time'])
        if measurement == 'O2':
           ventilator_for_chris.append(timepoints['raw']['O2'])
        elif measurement == 'MVe':
           ventilator_for_chris.append(timepoints['processed']['MVe'])
        elif measurement == 'Co2':
            ventilator_for_chris.append(timepoints['raw']['CO2'])
        else: return "Measure "+measurement+" not supported."
    return json.dumps({"timestamps": timestamps, "measurements": ventilator_for_chris})

@app.route('/data')
def get_ventilator_data():
    global ventilators
    ventilator_for_chris = []
    patientid = int(request.args.get('patientid'))
    measurement = request.args.get('measurement')
    seconds = int(request.args.get('seconds'))
    print(patientid, measurement, seconds)
    all_about_ventilator = None
    for p in map_patients_to_ventilator:
        if p.id == patientid:
            all_about_ventilator = map_patients_to_ventilator[p].get_last_seconds(seconds)
    if all_about_ventilator is None:
        return "Patient "+str(patientid)+" not found"
    for timepoints in all_about_ventilator:
        if measurement == 'O2':
           ventilator_for_chris.append(timepoints['raw']['O2'])
        elif measurement == 'MVe':
           ventilator_for_chris.append(timepoints['processed']['MVe'])
        elif measurement == 'Co2':
            ventilator_for_chris.append(timepoints['raw']['CO2'])
        else: return "Measure "+measurement+" not supported."
    return json.dumps(ventilator_for_chris)

@app.route('/patient_by_id')
def get_patient_by_id():
    global patients
    global map_patients_to_ventilator
    patientid = int(request.args.get('patientid'))
    for p in patients:
        if p.id == patientid:
            p.set_severity(map_patients_to_ventilator[p].severity_score())
            return json.dumps(p, default=lambda o: o.__dict__)
    return 'patient not found'




## how to run in terminal
# export PYTHONPATH="/home/svea/Desktop/Wo_der_server_lauft/HackaTUMCovid20/"
# source ./Hackathon/venv/bin/activate
# python Hackathon/app.py

# Does not execute this
#From terminal, we need export PYTHONPATH="/home/svea/Desktop/HackaTUMCovid20;/home/svea/Desktop/HackaTUMCovid20/Hackathon"

if __name__ == '__main__':
    args = sys.argv
    if "debug" in args:
        app.run(host='0.0.0.0', port=5001)
    else:
        app.run(host='0.0.0.0')

