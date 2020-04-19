from datetime import datetime

class Patients:
    def __init__(self, id=1000, name='Egon', age=4, smoker=True, bmi=20, rscore=5, state='back', last_time_wendet=None, delta=None, severity=None):
        self.id = id
        self.name = name
        self.age = age
        self.smoker = smoker
        self.bmi = bmi
        self.rscore = rscore
        self.severity = severity
        self.state = state
        self.delta = delta
        self.last_time_wendet = last_time_wendet

    def set_severity(self, severity):
        self.severity = severity
        return

    def change_state(self):
        if self.state == 'back':
           self.state = 'front'
        elif self.state == 'front':
           self.state = 'back'
        self.last_time_wendet = datetime.now()
        return

    def set_delta(self):
        self.delta = datetime.now()-self.last_time_wendet
        return


def get_patients():
    List_with_patients = []

    List_with_patients.append(Patients(1000, 'K. E.', 57, False, 25, 4, 'back', datetime.now()))
    List_with_patients.append(Patients(1001, 'K. E.', 61, False, 20, 6, 'back', datetime.now()))
    List_with_patients.append(Patients(1002,'F. U.', 45, True, 30, 8, 'back', datetime.now()))
    List_with_patients.append(Patients(1003,'D. M.', 60, False, 22, 4, 'back', datetime.now()))
    List_with_patients.append(Patients(1004, 'I. S.', 81, False, 23, 7, 'back', datetime.now()))
 #   List_with_patients.append(Patients(1005,'B. H.', 52, True, 18, 6))
  #  List_with_patients.append(Patients(1006,'J. L.', 39, False, 21, 2))
   # List_with_patients.append(Patients(1007, 'P. W.', 59, False, 21, 4))
    return List_with_patients


