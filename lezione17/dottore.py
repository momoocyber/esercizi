from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name, last_name, specialization, parcel):
        super().__init__(first_name, last_name)
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")
            self.__specialization = None

        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float!")
            self.__parcel = None

    def setSpecialization(self, specialization):
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcel):
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float!")

    def getSpecialization(self):
        return self.__specialization

    def getParcel(self):
        return self.__parcel

    def isAValidDoctor(self):
        if self.getAge() > 30:
            print(f" Doctor {self.first_name} {self.last_name} is valid! ")
            return True
        else:
            print(f" Doctor {self.first_name} {self.last_name} is not valid! ")
            return False
    def doctorGreet(self):
        self.greet()
        print(f" Sono un medico {self.__specialization} ")