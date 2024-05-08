class Persona:
    def __init__(self, name: str, surname: str, ssn: str) -> None:

        """
        
        
        """
        
        self.ID: int = 1
        self._name: str = name
        self._surname: str = surname
        self._ssn: str = ssn
        self._birth_date : str= "24/12/1994"
        self.birth_place: str = "Roma"

    def get_ssn(self) -> str:
        """
        this function returns the ssn value
        input: None
        return: self._ssn : str, the function returns the ssn value

        """
        return self._ssn    

    def set_ssn(self, ssn: str) -> None:
        """
        This function set the attribute ssn
        input:  ssn : str, the parametrs contain the ssn
        return: none
        
        
        """

        raise Exception("you cannot modify this value")


    def get_name(self) -> str:
        """
        this function returns a person's name
        input: None
        return: self._name : str, the function returns the person's name
        
        """

        return self._name

    def set_name(self, name: str):
        """
        
        This function set the attribute name
        input : name :str, the parameter contains the user's name
        return: None
        """

        raise Exception("you cannot modify the name!")
        




persona_1: Persona= Persona(name="Mohamed", surname="Morjani", ssn="MRJMMD01H501H")
persona_2: Persona= Persona(name="Mirko", surname="Rossi", ssn="MRKDGH01C09H501H")



print(persona_1.get_name())
#print(persona_2.get_ssn())

queue: list[Persona]= [persona_1, persona_2]

for persona in queue:

    print(persona.get_ssn())
