import copy
import sys
from datetime import date, time, timedelta

from flask import Flask, request
import json
from time import sleep
import time
import requests
from Hackathon import Patient
from Hackathon import VentilatorOld as Ventilator
from collections import OrderedDict
from _thread import start_new_thread
from datetime import datetime

# link to communicate externally: http://129.187.212.1:5000/patient?sorting=rscore
# Link to communicate internally: curl localhost:5001/tdata?"patientid=1000&seconds=300&measurement=O2"

app = Flask(__name__)

mock = False

patients = Patient.get_patients()


## ?
def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    #if isinstance(obj, time):
    #    serial = obj.isoformat()
    #    return serial

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial

    if isinstance(obj, timedelta):
        serial = obj.total_seconds()
        return serial

    return obj.__dict__


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


## super ugly hack
def continous_update_of_ventilators():
    timeout = 600
    while 1 == 1:
        sleep(0.2)
        try:
            r = requests.get('https://api.theopenvent.com/exampledata/v2/data', verify=False, timeout=timeout)
            timeout = 0.6
            data = r.json()
            for key in data:
                for v in ventilators:
                    if data[key]['device_id'] == v.id:
                        v.add_data(data[key])
        except Exception as ex:
            print(ex)
            for v in ventilators:
                for diff in [-1,0,1]:
                    last = v.get_last_seconds(1)[0]
                    current = copy.deepcopy(last)
                    current["time"] = int(time.time()+diff)
                    v.add_data(current)

start_new_thread(continous_update_of_ventilators, ())

map_patients_to_ventilator = OrderedDict()
map_ventilators_to_patients = OrderedDict()
for idx, p in enumerate(patients):
    map_patients_to_ventilator[p] = ventilators[idx]
    map_ventilators_to_patients[ventilators[idx]] = p


@app.route('/patient')
def get_patient_list():
    sorting = request.args.get('sorting')
    global patients
    global map_patients
    global serialize
    global mock
    for p in map_patients_to_ventilator:
        p.set_severity(map_patients_to_ventilator[p].severity_score(mock)[0], mock)
        p.set_delta()
    patients_new = patients
    if sorting == 'rscore':
        patients_new = sorted(patients, key=lambda patient: patient.rscore, reverse=True)
    elif sorting == 'severity':
        patients_new = sorted(patients, key=lambda patient: patient.severity, reverse=True)
    elif sorting == 'age':
        patients_new = sorted(patients, key=lambda patient: patient.age, reverse=True)
    elif sorting == 'delta':
        patients_new = sorted(patients, key=lambda patient: patient.delta, reverse=True)

    return json.dumps(patients_new, default=serialize)


# user = request.args.get('name')

#
# return patients

@app.route('/tdata')
def get_tventilator_data():
    global ventilators
    global mock
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
        return "Patient " + str(patientid) + " not found"
    timestamps = []
    for timepoints in all_about_ventilator:
        timestamps.append(timepoints['time'])
        if measurement == 'O2':
            if (all_about_ventilator[0]["device_id"] == 4242) & mock:
                ventilator_for_chris.append(Ventilator.mock(float(timepoints['processed']['ExpiredO2']), timepoints['time']))
            else:
                ventilator_for_chris.append(float(timepoints['processed']['ExpiredO2']))
        elif measurement == 'MVe':
            ventilator_for_chris.append(float(timepoints['processed']['MVe']))
        elif measurement == 'Co2':
            ventilator_for_chris.append(float(timepoints['raw']['CO2']))
        elif measurement == 'frequency':
            ventilator_for_chris.append(float(timepoints['processed']['frequency']))
        else:
            return "Measure " + measurement + " not supported."
    return json.dumps({"timestamps": timestamps, "measurements": ventilator_for_chris})


@app.route('/patient_by_id')
def get_patient_by_id():
    global patients
    global map_patients_to_ventilator
    patientid = int(request.args.get('patientid'))
    for p in patients:
        if p.id == patientid:
            p.set_severity(map_patients_to_ventilator[p].severity_score(mock)[0])
            p.set_delta()
            return json.dumps(p, default=serialize)
    return 'patient not found'


@app.route('/ventilator_by_patienid')
def get_ventilator():
    global ventilators
    patientid = int(request.args.get('patientid'))
    for p in map_patients_to_ventilator:
        if p.id == patientid:
            all_about_ventilator = map_patients_to_ventilator[p].get_last_seconds(1)

    return json.dumps(all_about_ventilator, default=serialize)


@app.route('/backflip')
def change_state():
    global patients
    patientid = int(request.args.get('patientid'))
    for p in patients:
        if p.id == patientid:
            p.change_state()
            p.set_delta()
    return "changed state"


@app.route('/startmock')
def start_mocking():
    global mock
    mock = True
    return "data is now mocked"

@app.route('/endmock')
def end_mocking():
    global mock
    mock = False
    return "data is now not mocked"



## how to run in terminal
# export PYTHONPATH="/home/svea/Desktop/Wo_der_server_lauft/HackaTUMCovid20/"
# source ./Hackathon/venv/bin/activate
# python Hackathon/app.py

# Does not execute this
# From terminal, we need export PYTHONPATH="/home/svea/Desktop/HackaTUMCovid20;/home/svea/Desktop/HackaTUMCovid20/Hackathon"

if __name__ == '__main__':
    args = sys.argv
    if "debug" in args:
        app.run(host='0.0.0.0', port=5001)
    else:
        app.run(host='0.0.0.0')
