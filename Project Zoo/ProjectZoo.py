

class Animal:

    def __init__(self, name : str, species : str, age : int, height : float, width : float, preferred_habitat : str) -> None:

        self.name= name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=preferred_habitat
        self.healt= round(100*(1/age), 3)
        self.area= width*height

class Fence:
        
    def __init__(self, animali: list[Animal], area: float, temperature : float, habitat : str) -> None:
        self.area=area
        self.temperature=temperature
        self.habitat= habitat
        self.animali=animali


class Zookeeper:
     
    def __init__(self, name: str, surname: str, ID: str) -> None:
          
        self.name=name
        self.surname=surname
        self.ID=ID
        

    def add_animal(self, animal: Animal, fence: Fence):

        if animal.preferred_habitat== fence.habitat and fence.area-animal.area >0:
            print("animale aggiunto")
            fence.animali.append(animal)
            return  fence.animali 
        else:
            print("impossibile aggiungere l'animale")
            return None

              
                
        

class Zoo:
     
    def __init__(self, list_zookeeper: list[Zookeeper], list_fences: list[Fence]) -> None:
          
        self.list_zookeeper: list[Zookeeper]= list_zookeeper
        self.list_fences: list[Fence]= list_fences




animals = [
    Animal("Leo", "Lion", 5, 1.5, 2.0, "Savannah"),
    Animal("Tiger", "Tiger", 6, 1.7, 2.2, "Savannah"),
    Animal("Giraffe", "Giraffe", 8, 4.0, 1.5, "Savannah"),
    Animal("Elephant", "Elephant", 10, 3.5, 4.0, "Forest"),
    Animal("Zebra", "Zebra", 4, 1.6, 2.0, "Savannah"),
    Animal("Bear", "Bear", 7, 2.0, 1.8, "Forest"),
    Animal("Penguin", "Penguin", 3, 0.5, 0.3, "Aquatic"),
    Animal("Lemur", "Lemur", 2, 0.6, 0.4, "Forest"),
    Animal("Crocodile", "Crocodile", 9, 2.5, 3.0, "Aquatic"),
    Animal("Kangaroo", "Kangaroo", 5, 1.8, 1.0, "Savannah")
]

# Creazione di 5 istanze di Fence
fences = [
    Fence([], 150.0, 25.0, "Savannah"),
    Fence([], 100.0, 20.0, "Forest"),
    Fence([], 80.0, 15.0, "Aquatic"),
    Fence([], 200.0, 30.0, "Savannah"),
    Fence([], 120.0, 22.0, "Savannah")
]

# Creazione di 3 istanze di Zookeeper
zookeepers = [
    Zookeeper("John", "Doe", "123456"),
    Zookeeper("Alice", "Smith", "654321"),
    Zookeeper("Bob", "Johnson", "987654")
]

# Creazione di un'istanza di Zoo
zoo = Zoo(zookeepers, fences)


for i, fence in enumerate(fences):
    print(f"Recinzione {i+1}:")
    for animal in fence.animali:
        print(f"- {animal.name}, Specie: {animal.species}, Età: {animal.age}, Altezza: {animal.height}, Larghezza: {animal.width}, Habitat Preferito: {animal.preferred_habitat}")

# Stampa delle informazioni sugli addetti
print("\nInformazioni sugli addetti:")
for zookeeper in zookeepers:
    print(f"Nome: {zookeeper.name}, Cognome: {zookeeper.surname}, ID: {zookeeper.ID}")


zookeeper_instance = Zookeeper("Jane", "Doe", "987654")


zookeeper_instance.add_animal(animals, fences)