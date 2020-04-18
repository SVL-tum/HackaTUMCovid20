
class Patients:
    def __init__(self, id=1000, name='Egon', age=4, smoker=True, bmi=20, rscore=5, severity=None):
        self.id = id
        self.name = name
        self.age = age
        self.smoker = smoker
        self.bmi = bmi
        self.rscore = rscore
        self.severity = severity

    def set_severity(self, severity):
        self.severity = severity
        return

def get_patients():
    List_with_patients = []

    List_with_patients.append(Patients(1000, 'K. E.', 57, False, 25, 4))
    List_with_patients.append(Patients(1001, 'K. E.', 61, False, 20, 6))
    List_with_patients.append(Patients(1002,'F. U.', 45, True, 30, 8))
    List_with_patients.append(Patients(1003,'D. M.', 60, False, 22, 4))
    List_with_patients.append(Patients(1004, 'I. S.', 81, False, 23, 7))
 #   List_with_patients.append(Patients(1005,'B. H.', 52, True, 18, 6))
  #  List_with_patients.append(Patients(1006,'J. L.', 39, False, 21, 2))
   # List_with_patients.append(Patients(1007, 'P. W.', 59, False, 21, 4))
    return List_with_patients


