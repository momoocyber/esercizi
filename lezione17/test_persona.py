import unittest
from paziente import Paziente
from dottore import Dottore
from persona import Persona
from fattura import Fattura

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("Fabio", "Seri")

    def test_initialization(self):
        self.assertEqual(self.persona.getName(), "Fabio")
        self.assertEqual(self.persona.getLastName(), "Seri")
        self.assertEqual(self.persona.getAge(), 0)

    def test_setName(self):
        self.persona.setName("Claudio")
        self.assertEqual(self.persona.getName(), "Claudio")

    def test_setLastName(self):
        self.persona.setLastName("Ronaldo")
        self.assertEqual(self.persona.getLastName(), "Ronaldo")

    def test_setAge(self):
        self.persona.setAge(27)
        self.assertEqual(self.persona.getAge(), 27)

class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Cristiano", "Messi", "Ginecologo", 100.0)

    def test_initialization(self):
        self.assertEqual(self.dottore.getSpecialization(), "Ginecologo")
        self.assertEqual(self.dottore.getParcel(), 100.0)

    def test_isValidDoctor(self):
        self.dottore.setAge(40)
        self.assertEqual(self.dottore.isAValidDoctor(), True)

class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente("Kyle", "Jenner", "AAAA2")

    def test_initialization(self):
        self.assertEqual(self.paziente.getIdCode(), "AAAA2")

class TestFattura(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Cristiano", "Messi", "Ginecologo", 100.0)
        self.dottore.setAge(42)
        self.paziente1 = Paziente("Fabio", "Seri", "BBBB3")
        self.paziente2 = Paziente("Claudio", "Ronaldo", "CCCC4")
        self.fattura = Fattura([self.paziente1, self.paziente2], self.dottore)

    def test_initialization(self):
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary(), 200.0)

    def test_addPatient(self):
        new_patient = Paziente("Francesco", "Totti", "CAP10")
        self.fattura.addPatient(new_patient)
        self.assertEqual(self.fattura.getFatture(), 3)
        self.assertEqual(self.fattura.getSalary(), 300.0)

    def test_removePatient(self):
        self.fattura.removePatient("BBBB3")
        self.assertEqual(self.fattura.getFatture(), 1)
        self.assertEqual(self.fattura.getSalary(), 100.0)

if __name__ == '__main__':
    unittest.main()
