

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
        self.fence= None

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

        if animal.preferred_habitat == fence.habitat and fence.area-animal.area >0:
            print("animale aggiunto!")
            fence.animali.append(animal)
            fence.area-=animal.area
            animal.fence= fence
            
        else:
            print("impossibile aggiungere l'animale")
            

    def remove_animal(self, animal: Animal, fence: Fence):

        fence.animali.remove(animal)
        print("l'animale è stato rimosso!")

        fence.area+=animal.area
        print(f"Area disponibile {fence.area}")

        return fence.area


    def feed(self, animal : Animal):

        incremento_vita= (animal.healt *1)/100
        animal.healt+=incremento_vita
        

        incremento_height= (animal.height*2)/100
        incremento_widht= (animal.width*2)/100

        animal.height+=incremento_height
        animal.width+= incremento_widht
        new_area= animal.width* animal.height

        

        if (animal.fence.area - new_area) > 0:

            print(f"widht è stata incrementata del 2 % : {animal.width}, height + 2%  : {animal.height} ") 
            print(f"la vita è stata incrementata del 1 % : {animal.healt}")

            return animal.healt, animal.height, animal.width
    


    def clean(self, fence : Fence):

        time : float = 0
        area_residua= fence.area
        area_occupata= fence.area
        for i in fence.animali:
            area_residua= fence.area - i.area
            area_occupata=area_occupata+ i.area
       
        if area_residua ==  0 :
            print(f"area occupata: {area_occupata}")
            return area_occupata
        else:
            time= area_occupata/area_residua
            print(f"tempo occupato {time}")

        return time


            
        
class Zoo:
     
    def __init__(self, list_zookeeper: list[Zookeeper], list_fences: list[Fence]) -> None:
          
        self.list_zookeeper: list[Zookeeper]= list_zookeeper
        self.list_fences: list[Fence]= list_fences

    def describe_zoo(self):

        print("\nGuardians:\n")
        for i in self.list_zookeeper:
            print(f"name={i.name}, surname={i.surname}, id={i.ID}")

        print("\nFences:\n")

        for i in self.list_fences:
            print(f"Area={i.area}, temperature={i.temperature}, habitat={i.habitat}")   

        print("\nwith animals:\n")

        for i in self.list_fences: 
            for j in i.animali:
                print(f"name={j.name}, species={j.species}, age={j.age}")

        print("##############################")






animals: Animal =  Animal("Leo", "Lion", 5, 1.5, 2.0, "Savannah")
animals_2: Animal=  Animal("Teo", "Tiger", 6, 3.5, 4.0, "Jungle" ) 
#animals_list : list[Animal]= [animals, animals_2]

fences : Fence = Fence([], 150.0, 25.0, "Savannah")
fences_2: Fence = Fence([], 170.0, 35.0, "jungle")
#fences_list: list[Fence]  = [fences, fences_2] 

zookeepers =  Zookeeper("John", "Doe", "123456")
zookeeper_instance = Zookeeper("Jane", "Doe", "987654")
#zookeepers_list: list[Zookeeper]= [zookeepers, zookeeper_instance]

zoo: Zoo= Zoo([zookeeper_instance, zookeepers], [fences, fences_2])


zookeeper_instance.add_animal(animals, fences)
#zookeeper_instance.remove_animal(animals, fences)
zookeeper_instance.feed(animals)
zookeeper_instance.clean(fences)
zoo.describe_zoo()

