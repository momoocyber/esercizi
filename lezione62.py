class Student:
    def __init__(self, name:str, study_program:str, age: int, gender:str ) -> None:
        self.name=name
        self.study_program=study_program
        self.age=age
        self.gender=gender


    def print_info(self):
        print(f"{self.name}, {self.study_program}, {self.age}, {self.gender}")

        





student_1: Student= Student(name="mario", study_program="cyber", age= 20, gender= "M")       
student_2: Student= Student(name="gigio", study_program="cyber", age= 26, gender= "M")   
student_3: Student= Student(name="claudio", study_program="cyber", age= 30, gender= "M")    

student_1.print_info()
student_2.print_info()
student_3.print_info() 




class Animal:
    def __init__(self, name: str , legs: int) -> None:
        self._name=name
        self._legs=legs


    def get_name(self) -> str:
        
        return self._name 
    
    def set_name(self, name: str):
        self._name= name
        
    
    def get_legs(self) -> int:
        
        return self._legs
    
    def set_legs(self, legs: int):
        self._legs=legs


    def print_info(self):
        print(f"name: {self._name}, legs: {self._legs}")  




animal_1: Animal= Animal(name="dog", legs=4)  
animal_2: Animal= Animal(name="cat", legs=4)   

print(animal_1.get_name())
print(animal_2.get_name())
print(animal_1.get_legs())
print(animal_2.get_legs())
animal_1.set_name("coccodrillo")
animal_2.set_name("pavone")
animal_1.set_legs(4)
animal_2.set_legs(2)

animal_1.print_info()
animal_2.print_info()



class Food:
    def __init__(self, name:str, price:int, description:str ) -> None:
        self.name=name
        self.price=price
        self.description=description

food_1: Food=Food(name="pizza", price=5, description="very good food")
food_2: Food=Food(name="pasta", price=9, description="very nice")
food_3: Food=Food(name="burger", price=6, description="very saucy")

class Menu:
    def __init__(self, list_foods: list= []) -> None:

        self.list_foods= list_foods

    def add_food(self, food : Food):
        self.list_foods.append(food)

        return self.list_foods

    def remove_food(self, food : Food):
        self.list_foods.remove(food)

        return self.list_foods

    def print_prices(self):
        for i in self.list_foods:
            print(f"{i.name}, {i.price}")   

    def get_average_price(self):
        prices=0
        for i in self.list_foods:
            prices+=i.price
        average= prices/len(self.list_foods)
        return average    


            


menu: Menu= Menu(list_foods=[food_1, food_2, food_3 ])
food_4: Food= Food(name="cake", price=4, description="very sweet")
menu.add_food(food_4)
menu.remove_food(food_2)
menu.print_prices()
print(menu.get_average_price())
