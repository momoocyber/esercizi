from dottore import Dottore
from paziente import Paziente
class Fattura:

    def __init__(self, patients: list[Paziente], doctor : Dottore):
        self.patients = patients
        self.doctor = doctor
        if doctor.isAValidDoctor():
            self.fatture = len(patients)
            self.salary = 0
        else:
            self.patients = None
            self.doctor = None
            self.fatture = None
            self.salary = None
            print("Non è possibile creare la classe fattura poiché il dottore non è valido!")

    

    def getSalary(self):

        self.fatture= len(self.patients)
        parcella= self.doctor.getParcel()* self.fatture
        return parcella
        
            

    def getFatture(self):
        if self.fatture is not None:
            self.fatture= len(self.patients)
            return self.fatture
        else:
            return None

    def addPatient(self, newPatient):
        if self.patients is not None:
            self.patients.append(newPatient)
            self.fatture = len(self.patients)
            self.salary = self.getSalary()
            print(f"Alla lista del Dottor {self.doctor.last_name} è stato aggiunto il paziente {newPatient.codice_identificativo}")
        else:
            print("Non è possibile aggiungere pazienti perché il dottore non è valido!")

    def removePatient(self, patient_id):
        if self.patients is not None:
            for patient in self.patients:
                if patient.__idCode == patient_id:
                    self.patients.remove(patient)
                    self.fatture = len(self.patients)
                    self.salary = self.getSalary()
                    print(f"Alla lista del Dottor {self.doctor.last_name} è stato rimosso il paziente {patient_id}")
                    break
            else:
                print("Il paziente non è presente nella lista.")
        else:
            print("Non è possibile rimuovere pazienti perché il dottore non è valido!")
