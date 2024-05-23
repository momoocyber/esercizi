# 9-1. Restaurant: Make a class called Restaurant. The __init__()
# method for Restaurant should store two attributes: a restaurant_name 
# and a cuisine_type. Make a method called describe_restaurant() that 
# prints these two pieces of information, and a method called
# open_restaurant() that prints a message indicating that
# the restaurant is open. Make an instance called restaurant from
# your class. Print the two attributes individually, and then call
# both methods.

"""
class Restaurant:

    def __init__(self, name: str, type: str) -> None:
        self.name= name
        self.type=type

    def describe_restaurant(self):

        print(f"Name: {self.name}, Type: {self.type}")    


    def open_restaurant(self):

        print(f"The Restaurant: {self.name} is open")    




ristorante: Restaurant= Restaurant("osteria dell' orologio", "gourmet")

ristorante.describe_restaurant()
ristorante.open_restaurant()



# 9-2. Three Restaurants: Start with your class from Exercise 9-1.
# Create three different instances from the class, and call 
# describe_restaurant() for each instance.


ristorante_2: Restaurant= Restaurant("Ciccio food", "panineria")
ristorante_3: Restaurant= Restaurant("Mcdonalds", "fast food")
ristorante_2.describe_restaurant()
ristorante_3.describe_restaurant()


"""

# 9-3. Users: Make a class called User. Create two attributes 
# called first_name and last_name, and then create several other 
# attributes that are typically stored in a user profile. Make a method
# called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized
# greeting to the user. Create several instances representing different 
# users, and call both methods for each user.

"""
class User:

    def __init__(self, first_name:str, last_name : str, age:int) -> None:

        self.first_name= first_name
        self.last_name= last_name
        self.age= age

    def describe_user(self):

        print(f"Nome: {self.first_name}, Cognome: {self.last_name}, Età: {self.age}")    
        

    def greet_user(self):

        print(f"hello {self.first_name}")    


user: User= User("Paolo", "Sorriso", 20)        

user.describe_user()
user.greet_user()
"""

# 9-4. Number Served: Start with your program from Exercise 9-1. 
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class. Print the 
# number of customers the restaurant has served, and then change this 
# value and print it again. Add a method called set_number_served()
# that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again. Add a 
# method called increment_number_served() that lets you increment the 
# number of customers who’ve been served. Call this method with any
# number you like that could represent how many customers were served in,
# say, a day of business. 


from typing import Any


class Restaurant:

    def __init__(self, name: str, type: str) -> None:
        self.name= name
        self.type=type
        self.number_served=0

    def describe_restaurant(self):

        print(f"Name: {self.name}, Type: {self.type}")    


    def open_restaurant(self):

        print(f"The Restaurant: {self.name} is open")   

    def set_number(self, number_served):
        self.number_served= number_served

    def increment_number(self, number):

        self.number_served+= number

        return self.number_served


            
  
ristorante: Restaurant= Restaurant("osteria dell' orologio", "gourmet")

ristorante.describe_restaurant()
print(ristorante.number_served)
ristorante.set_number(3)
print(ristorante.number_served)

ristorante.increment_number(5)
print(ristorante.number_served)


# 9-5. Login Attempts: Add an attribute called login_attempts to 
# your User class from Exercise 9-3. Write a method called 
# increment_login_attempts() that increments the value of login_attempts
# by 1. Write another method called reset_login_attempts() that resets
# the value of login_attempts to 0. Make an instance of the User class and 
#    call increment_login_attempts() several times. Print
#    the value of login_attempts to make sure it was incremented properly,
#    and then call reset_login_attempts(). Print login_attempts again 
#    to make sure it was reset to 0.


class User:

    def __init__(self, first_name:str, last_name : str, age:int, login_attempt: int) -> None:

        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.login_attempt= login_attempt

    def describe_user(self):

        print(f"Nome: {self.first_name}, Cognome: {self.last_name}, Età: {self.age}")    
        

    def greet_user(self):

        print(f"hello {self.first_name}")    

    def increment_login_attempts(self): 

        self.login_attempt+=1
        
        return self.login_attempt  
        
    def reset_login_attempts(self):

        self.login_attempt=0

        return self.login_attempt

user: User= User("Paolo", "Sorriso", 20, 0)        

user.describe_user()
user.greet_user()

user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempt)

user.reset_login_attempts()

print(user.login_attempt)



# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant
# class you wrote in Exercise 9-1  or Exercise 9-4. Either version of 
# the class will work; just pick the one you like better. Add an attribute
#  called flavors that stores a list of ice cream flavors. Write a method
#  that displays these flavors. Create an instance of IceCreamStand, and 
#  call this method. 


class IceCreamStand(Restaurant):
    def __init__(self, name: str, type: str, flavors : list) -> None:
        super().__init__(name, type)
        self.flavors=flavors

    def display(self):
        for i in self.flavors:
            print(i)    



gelato=IceCreamStand("Polo nord","gelataio",["cioccolato", "panna", "pistacchio"])
gelato.display()
gelato.describe_restaurant()


# 9-7. Admin: An administrator is a special kind of user. Write a class
#  called Admin that inherits from the User class you wrote in 
# Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, 
# that stores a list of strings like "can add post", "can delete post",
# "can ban user", and so on. Write a method called show_privileges() 
# that lists the administrator’s set of privileges. Create an instance 
# of Admin, and call your method. 

"""
class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, login_attempt: int, privileges: list) -> None:
        super().__init__(first_name, last_name, age, login_attempt)
        self.privileges=privileges

    def show_privileges(self):

        for i in self.privileges:
            print(i)

admin: Admin= Admin("Cristiano", "Ronaldo", 20, 0, ["can add post","can delete post","can ban user" ])   
admin.describe_user()
admin.show_privileges()      

"""
# 9-8. Privileges: Write a separate Privileges class. 
#    The class should have one attribute, privileges, that 
#    stores a list of strings as described in Exercise 9-7.
#    Move the show_privileges() method to this class. Make a Privileges
#     instance as an attribute in the Admin class. Create a new instance
#     of Admin and use your method to show its privileges.

class Privileges:

    def __init__(self, list:list) -> None:
        self.list=list

    def show_privileges(self):

        for i in self.list:
            print(i)    

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, login_attempt: int, privileges :Privileges ) -> None:
        super().__init__(first_name, last_name, age, login_attempt)
        self.privileges= privileges

    

privilegi: Privileges= Privileges(["can add post","can delete post","can ban user" ])        

admin: Admin= Admin("Cristiano", "Ronaldo", 20, 0, privilegi) 
 
admin.describe_user()
admin.privileges.show_privileges()



# 9-9. Battery Upgrade: Use the final version of electric_car.py from 
# this section. Add a method to the Battery class called upgrade_battery().
# This method should check the battery size and set the capacity to 65 if
# it isn’t already. Make an electric car with a default battery size,
# call get_range() once, and then call get_range() a second time after
# upgrading the battery. You should see an increase in the car’s range.        