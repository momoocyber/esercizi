import time

# 8-1. Message: Write a function called display_message()
# that prints one sentence telling everyone what you are 
# learning about in this chapter. Call the function, and 
# make sure the message displays correctly.


def display_message():
    print("bla bla bla")

display_message()



# 8-2. Favorite Book: Write a function called favorite_book() 
# that accepts one parameter, title. The function should print a message, 
# such as "One of my favorite books is Alice in Wonderland". Call the function, 
# making sure to include a book title as an argument in the function call.

def favorite_books(title : str) -> None:
    print(f"my favorite book is {title}")

title : str =input("inserisci il titolo del libro")
favorite_books(title)


# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size
# and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt 
# and the message printed on it. Call the function once using positional 
# arguments to make a shirt. Call the function a second time using keyword 
# arguments.


def make_shirt(size : str, text : str)-> None:
    print(f"the size is: {size}, the text is: {text}")

    
size: str= input("inserisci size")
text: str= input("inserisci testo sulla maglietta")

make_shirt(size, text)



# 8-4. Large Shirts: Modify the make_shirt() function so that shirts 
# are large by default with a message that reads I love Python. Make 
# a large shirt and a medium shirt with the default message, and a shirt 
# of any size with a different message.

def make_shirt(size : str, text : str,  default_msg: str = "I love Python")-> None:
    if size=="medium" or size=="large":
        print(f"{size},{default_msg} ")
    else:
        print(f"the size is: {size}, the text is: {text}")

    
text: str= input("inserisci testo sulla maglietta")

size: str= input("inserisci size")


make_shirt(size, text)



# 8-5. Cities: Write a function called describe_city() 
# that accepts the name of a city and its country. The function should print 
# a simple sentence, such as Reykjavik is in Iceland. Give the parameter for 
# the country a default value. Call your function for three different cities,
# at least one of which is not in the default country.


def describe_city(city: str, country: str="italy")->None:
    print(f"{city} is in {country}")

describe_city("rome")
describe_city("venezia")
describe_city("new york", "usa")


# 8-6. City Names: Write a function called city_country() that takes in
# the name of a city and its country. The function should return a string 
# formatted like this: "Santiago, Chile". Call your function with at least 
# three city-country pairs, and print the values that are returned.


def describe_city(city: str, country: str)->str:
    

    return f"{city}, {country}"

string : str= describe_city("santiago","chile")
string_2 : str= describe_city("roma","italy")
string_3 : str= describe_city("dubai","emirati")

print(string)
print(string_2)
print(string_3)


# 8-7. Album: Write a function called make_album() that builds a
# dictionary describing a music album. The function should take in an artist
# name and an album title, and it should return a dictionary containing these 
# two pieces of information. Use the function to make three dictionaries 
# representing different albums. Print each return value to show that the  
# dictionaries are storing the album information correctly. Use None to add 
# an optional parameter to make_album() that allows you to store the number 
# of songs on an album. If the calling line includes a value for the number 
# of songs, add that value to the album’s dictionary. Make at least one new 
# function call that includes the number of songs on an album.


def make_album(artist_name, album_title, num_song= None) -> dict:
    album = {"artist": artist_name, "title": album_title}
    if num_song!= None:
        album["num_songs"]= num_song
    return album  


album_1 = make_album("Artist1", "Album1")
album_2 = make_album("Artist2", "Album2")
album_3 = make_album("Artist3", "Album3", 11)


print(album_1)
print(album_2)
print(album_3)



# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that 
# information, call make_album() with the user’s input and print the dictionary 
# that’s created. Be sure to include a quit value in the while loop.


def make_album(artist_name, album_title, num_song= None) -> dict:
    album = {"artist": artist_name, "title": album_title}
    if num_song!= None:
        album["num_songs"]= num_song
    return album  


i : int =0
while i<1:
    artist : list= input("inserisci il nome del artista")
    
    album: list=input("inserisci il titolo dell'album")
    
    i=i+1




album_1 = make_album("Artist1", "Album1")
album_2 = make_album("Artist2", "Album2")
album_3 = make_album("Artist3", "Album3", 11)
album_4 = make_album(artist, album)

print(album_1)
print(album_2)
print(album_3)
print(album_4)



# 8-9. Messages: Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints each text message.

def show_message(list):
    for i in list:
        print(i)

list   : list = ["ciao come stai", "paolo", "bonolis"]

show_message(list)




# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and moves each 
# message to a new list called sent_messages as it’s printed. After calling the function,
# print both of your lists to make sure the messages were moved correctly.


#def show_message(list):
#    for i in list:
#        print(i)

def send_message(list_1):
    for i in list_1:
        print(i)
        sent_message= list_1[:]

    return sent_message


list_1   : list = ["ciao come stai", "paolo", "bonolis"]

# show_message(list_1)
send= send_message(list_1)
print(f"questa è la nuova lista {send}")




# 8-11. Archived Messages: Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original
# list has retained its messages.



def send_message(list_1):
    for i in list_1:
        print(i)
        sent_message= list_1[:]

    return sent_message


list_1   : list = ["ciao come stai", "paolo", "bonolis"]

# show_message(list_1)
send= send_message(list_1)
print(f"questa è la nuova lista {send}")
print(f"questa è la vecchia lista {list_1}")



# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. Call the function three times, 
# using a different number of arguments each time.


def items_sandwich(number:int):
    list_items : list=[]
    i=0
    while i< number:
        items= input("inserisci cosa vuoi mettere nel tuo sandwich")
        list_items.append(items)
        i=i+1

    return list_items


sandwich_1=items_sandwich(2)
print(f"promemoria primo panino : {sandwich_1}")
sandwich_2=items_sandwich(3)
print(f"promemoria secondo panino : {sandwich_2}")
sandwich_3=items_sandwich(4)
print(f"promemoria terzo panino : {sandwich_3}")



    
# 8-13. User Profile:  Build a profile of yourself by calling build_profile(), 
# using your first and last names and three other key-value pairs that describe you. 
# All the values must be passed to the function as parameters. The function then must 
# return a string such as "Eric Crow, age 45, hair brown, weight 67"


def build_profile(name: str, last_name: str, age: int,  nationality: str):
    profile= f"{name}, {last_name}, {age}, {nationality}"
 
    return profile


profile_1= build_profile("mario", "rossi", 33, "italiana")

print(profile_1)


# 8-14. Cars: Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. It should then accept 
# an arbitrary number of keyword arguments. Call the function with the required information and 
# two other name-value pairs, such as a color or an optional feature. Your function should work for 
# a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the 
# dictionary that’s returned to make sure all the information was stored correctly. 


def create_car(manufacturer, model, **kwargs):

    dict_cars= {"manufacturer": manufacturer , "model": model}
    dict_cars.update(kwargs)

    return dict_cars

car_1= create_car("ferrari", "purosangue", color="blue", year= 2023) 
print(car_1)


# 8-15. Printing Models: Put the functions for the example printing_models.py in a separate 
# file called printing_functions.py. Write an import statement at the top of printing_models.py, 
# and modify the file to use the imported functions.


# 8-16. Imports: Using a program you wrote that has one function in it, 
# store that function in a separate file. Import the function into your main program file, 
# and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import lezione44

lezione44.display_message()

lezione44.display_message_2()




# 8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
# and make sure they follow the styling guidelines described in this section.





# cosi si implementa il bubble sort

"""
def bubble_sort(numbers: list) -> list:

    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j]> numbers[j+1]:
                temp : int = numbers[j]
                numbers[j]= numbers[j+1]
                numbers[j+1]= temp
                
    return numbers
            

numbers : list = [i for i in range(10000, 1, -1)]
start : float = time.time()
ordinati : list =bubble_sort(numbers)
print(ordinati)
print(time.time()-start)


#improved bubble sort

def bubble_sort(numbers: list) -> list:

    for i in range(len(numbers)):
        for j in range(len(numbers)-i-1):
            if numbers[j]> numbers[j+1]:
                temp : int = numbers[j]
                numbers[j]= numbers[j+1]
                numbers[j+1]= temp
                
    return numbers
            

numbers : list =[i for i in range(10000, 1, -1)]

start : float = time.time()
ordinati : list =bubble_sort(numbers)
print(ordinati)
print(time.time()-start)


# bubble sort with flag

def bubble_sort(numbers: list) -> list:

    for i in range(len(numbers)):
        swap_flag : bool= False 
        for j in range(len(numbers)-i-1):
            if numbers[j]> numbers[j+1]:
                temp : int = numbers[j]
                numbers[j]= numbers[j+1]
                numbers[j+1]= temp
                swap_flag = True
        if swap_flag == False :
            return numbers
                    
    return numbers
            

numbers : list =[i for i in range(1, 10000)]

start : float = time.time()
ordinati : list = bubble_sort(numbers)
print(ordinati)
print(time.time()-start)



"""
