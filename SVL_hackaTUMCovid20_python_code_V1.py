# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

# HackaTUM Infineon Projekt
import numpy as np
import matplotlib.pyplot as plt
import json
import requests


print("Hello World")

# 1.Data Mining [json]
r = requests.get('http://api.theopenvent.com/exampledata/v2/data')
data = r.json()#json.loads("data.json")

# converts object into dict, array into list, null into none ...
for key in data:
    print(key['time'])
    
# 2.Data Cleaning [numpy, pandas]

# 3.Data Exploration (Correlationen, Feature Definition, Plots) [matplotlib, pandas]

# 4.Data Transfer (to App and Server)

# 5. Optional: Add data input from App about anamnesis



### Notes: clearing when patient changes!
###        add Password safety