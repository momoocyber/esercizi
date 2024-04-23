"""# 8-1. Message: Write a function called display_message()
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
"""

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


