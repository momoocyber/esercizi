# Mohamed Morjani
# 17/04/2024

print("hello world")

# 2-3. Personal Message: Use a variable to represent a person’s
# name, and print a message to that person. 
# Your message should be simple, such as,
# “Hello Eric, would you like to learn some Python today?”

name: str = "Mario"
message: str= f"Ciao {name}, ti va di imparare un po di python insieme"
print(message)


# 2-4. Name Cases: Use a variable to represent a person’s name,
# and then print that person’s name in lowercase,
# uppercase, and title case.

name_2: str = "Claudio"
uppercase_name: str = name_2.upper()
title_name: str = name_2.title()
lower_name: str = name_2.lower()
print(uppercase_name)
print(title_name)
print(lower_name)

# 2-5. Famous Quote: Find a quote from a famous person you admire.
# Print the quote and the name of its author.
# Your output should look something like the following, 
# including the quotation marks: Albert Einstein once said,
# “A person who never made a mistake never tried anything new.”

name_3: str = "Cristiano Ronaldo"
print(f"Una volta {name_3} disse:'SIUMMMMM'")

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time,
# represent the famous person’s name using a variable 
# called famous_person. Then compose your message and represent
# it with a new variable called message. Print your message. 

famous_person: str = "Cristiano Ronaldo"
message: str = (f"Una volta {famous_person} disse:'SIUMMMMM'")
print(message)

# 2-8. File Extensions: Python has a removesuffix() 
# method that works exactly like removeprefix(). 
# Assign the value 'python_notes.txt' to a variable called filename.
# Then use the removesuffix() method to display the filename without
# the file extension, like some file browsers do.

filename : str = "python_notes.txt"
filename_removed: str =filename.removesuffix(".txt")
print(filename_removed)


# 3-1. Names: Store the names of a few of your friends 
# in a list called names. Print each person’s name by 
# accessing each element in the list, one at a time.

names : list = ["messi", "neymar", "caputo", "babygang", "simbalarue"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])


# 3-2. Greetings: Start with the list you used in Exercise 3-1,
# but instead of just printing each person’s name, 
# print a message to them. The text of each message
# should be the same, but each message should be personalized 
# with the person’s name.

names : list = ["messi", "neymar", "caputo", "babygang", "simbalarue"]

print(f"ciao {names[0]}")
print(f"ciao {names[1]}")
print(f"ciao {names[2]}")
print(f"ciao {names[3]}")
print(f"ciao {names[4]}")

# 3-3. Your Own List: Think of your favorite mode of transportation,
# such as a motorcycle or a car, and make a list that stores several 
# examples. Use your list to print a series of statements about these 
# items, such as “I would like to own a Honda motorcycle.”

cars : list = ["mercedes", "bmw", "supra", "bugatti"]

print(f"mi piacerebbe avere una {cars[0]}")
print(f"mi piacerebbe avere una {cars[1]}")
print(f"mi piacerebbe avere una {cars[2]}")
print(f"mi piacerebbe avere una {cars[3]}")


# 3-4. Guest List: If you could invite anyone, 
# living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d 
# like to invite to dinner. Then use your list to print 
# a message to each person, inviting them to dinner.

guest_list : list = ["messi", "neymar", "caputo"]

print(f"sei invitato a cena {guest_list[0]}")
print(f"sei invitato a cena {guest_list[1]}")
print(f"sei invitato a cena {guest_list[2]}")

# 3-5. Changing Guest List: You just heard that one of
# your guests can’t make the dinner, so you need to send out 
# a new set of invitations. You’ll have to think of someone 
# else to invite.
#• Start with your program from Exercise 3-4. Add a print() 
# call at the end of your program, stating the name of the guest
# who can’t make it.
# Modify your list, replacing the name of the guest who can’t 
# make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person
# who is still in your list.



print(f"{guest_list[2]} non puo venire" )

guest_list.remove("caputo")
guest_list.insert(2, "cr7")
print(f"sei invitato a cena {guest_list[0]}")
print(f"sei invitato a cena {guest_list[1]}")
print(f"sei invitato a cena {guest_list[2]}")


# 3-6. More Guests: You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.


print("abbiamo a disposizione una tavola piu grande ")



guest_list.insert(0, "nazario")
guest_list.insert(1, "giacomo")
guest_list.append("totti")

print(f"sei invitato a cena {guest_list[0]}")
print(f"sei invitato a cena {guest_list[1]}")
print(f"sei invitato a cena {guest_list[2]}")
print(f"sei invitato a cena {guest_list[3]}")
print(f"sei invitato a cena {guest_list[4]}")
print(f"sei invitato a cena {guest_list[5]}")


# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.


print("scusate ma possiamo invitare solo 2 persone alla cena")

print(f"mi dispiace {guest_list[5]} ma non posso piu invitarti")
guest_list.pop(-1)

print(f"mi dispiace {guest_list[4]} ma non posso piu invitarti")
guest_list.pop(-1)

print(f"mi dispiace {guest_list[3]} ma non posso piu invitarti")
guest_list.pop(-1)

print(f"mi dispiace {guest_list[2]} ma non posso piu invitarti")
guest_list.pop(-1)

print(f"{guest_list}  siete ancora invitati")


# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

citta : list = ["losangeles", "dubai", "miami"]

print(citta)

x : list = sorted(citta)
print(x)
print(citta)

x : list = sorted(citta, reverse=True)
print(x)
print(citta)

citta.reverse()
print(citta)
citta.reverse()
print(citta)

citta.sort()
print(citta)
citta.sort(reverse=True)
print(citta)

# 3-9. Dinner Guests: Working with one of the programs
# from Exercises 3, use len() to print a message indicating 
# the number of people you’re inviting to dinner.

x: int = len(guest_list)
print("il numero di persone invitate e:", x)


# 3-10. Every Function: Think of things you could store in a list.
# For example, you could make a list of mountains, rivers, countries,
# cities, languages, or anything else you’d like. Write a program that
# creates a list containing these items and then uses each function
# introduced in this chapter at least once.

dream_list: list = ["marocco", "italia", "asroma"]
print(dream_list)

dream_list.insert(0, "mare")
dream_list.append("derossi")
dream_list.pop(-1)
x : list = sorted(dream_list)
dream_list.reverse()
y: int = len(dream_list)

print("questa è la lista modificata ", dream_list)
print("questa è la lunghezza", y)


# 6-1. Person: Use a dictionary to store information 
# about a person you know. Store their first name, last name,
# age, and the city in which they live. You should have keys 
# such as first_name, last_name, age, and city. Print each 
# piece of information stored in your dictionary.

person: dict = {"nome":"momo", "cognome":"morjani", "eta":23, "citta":"roma" }
print(f'nome: {person["nome"]}')
print("cognome:", person["cognome"])
print(" eta:", person["eta"])
print(" citta:", person["citta"])

# 6-2. Favorite Numbers: Use a dictionary to store people’s 
# favorite numbers. Think of five names, and use them as keys 
# in your dictionary. Think of a favorite number for each person, 
# and store each as a value in your dictionary. 
# Print each person’s name and their favorite number. 
# For even more fun, poll a few friends and get some actual 
# data for your program.

person: dict = {"paolo":5, "giacomo":9, "stefano":23, "max":3}
print(person)

# 6-3. Glossary: A Python dictionary can be used to model an 
# actual dictionary. However, to avoid confusion, let’s 
# call it a glossary.
# • Think of five programming words you’ve learned about 
# in the previous chapters. Use these words as the keys 
# in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted 
# output. You might print the word followed by a colon and 
# then its meaning, or print the word on one line and then 
# print its meaning indented on a second line. Use the newline 
# character (\n) to insert a blank line between each word-meaning
# pair in your output.

words: dict = {"int":"tipo per gli interi", "float":"tipo per i numeri decimali", "boolean":"restituisce true or false", "string":"tipo per le parole","cpu":"central processing unit" }

print(f'int significa: {words["int"]} \n')
print(f'float significa: {words["float"]} \n')
print(f'boolean significa: {words["boolean"]} \n')
print(f'string significa: {words["string"]} \n')
print(f'cpu significa: {words["cpu"]} \n')

# 6-7. People: Start with the program you wrote for Exercise 6-1.
# Make two new dictionaries representing different people, 
# and store all three dictionaries in a list called people.
# Loop through your list of people. As you loop through the list,
# print everything you know about each person.


person: dict = {"nome":"momo", "cognome":"morjani", "eta":23, "citta":"roma" }
person_2: dict = {"nome":"silvio", "cognome":"berlusca", "eta":100, "citta":"milano" }
person_3: dict = {"nome":"neymar", "cognome":"junior", "eta":30, "citta":"san paolo" }

person_list : list = [person, person_2, person_3]
print(person_list[0]['nome'], person_list[0]['cognome'], person_list[0]['eta'],person_list[0]['citta'])
print(person_list[1]['nome'], person_list[1]['cognome'], person_list[1]['eta'],person_list[1]['citta'])
print(person_list[2]['nome'], person_list[2]['cognome'], person_list[2]['eta'],person_list[2]['citta'])

# 6-8. Pets: Make several dictionaries, where each dictionary 
# represents a different pet. In each dictionary, include the kind 
# of animal and the owner’s name. Store these dictionaries in a list 
# called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pet: dict = {"razza":"pitbull", "proprietario":"ciccio"}
pet_2: dict = {"razza":"rotwailer", "proprietario":"tedua"}
pet_3: dict = {"razza":"bulldog", "proprietario":"marrakesh"}

pet_list : list = [pet, pet_2, pet_3]
print(pet_list[0]['razza'], pet_list[0]['proprietario'])
print(pet_list[1]['razza'], pet_list[1]['proprietario'])
print(pet_list[2]['razza'], pet_list[2]['proprietario']) 

# 6-9. Favorite Places: Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, and store one 
# to three favorite places for each person. To make this exercise a bit 
# more interesting, ask some friends to name a few of their favorite places. 
# Loop through the dictionary, and print each person’s name and their favorite
# places.

places: dict = {"mauro":["roma", "venezia"], "paolo":["miami","losangeles"],"sfera":"newyork"}

print(places)

# 6-10. Favorite Numbers: Modify your program from Exercise
# 6-2 so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers.

person: dict = {"paolo":[5, 3], "giacomo":[9, 4], "stefano":[23, 4] , "max":[3,4]}
print(person)

# 6-11. Cities: Make a dictionary called cities. Use the names of three 
# cities as keys in your dictionary. Create a dictionary of information 
# about each city and include the country that the city is in, its approximate
# population, and one fact about that city. The keys for each city’s dictionary 
# should be something like country, population, and fact. Print the name of each 
# city and all of the information you have stored about it.

cities: dict = {"venezia":["placed in italy ", "bellisima città costruita sull'acqua "], "roma":["placed in italy","città piu bella del mondo "],"new york":["placed in usa", "la grande mela "]}
print(cities)


# 6-12. Extensions: We’re now working with examples that are 
# complex enough that they can be extended in any number of ways.
# Use one of the example programs from this chapter, and extend it
# by adding new keys and values, changing the context of the program, 
# or improving the formatting of the output.


citta : list = ["losangeles", "dubai", "miami", "venezia","new york" ]

print(citta)

x : list = sorted(citta)
print(x)
print(citta)

x : list = sorted(citta, reverse=True)
print(x)
print(citta)

citta.reverse()
print(citta)

favorite_places: dict = {"mauro":["roma", "venezia"], "paolo":["miami","losangeles"],"sfera":"newyork"}
print(favorite_places)

citta : list = ["losangeles", "dubai", "miami", "venezia","new york" ]

print(citta)

x : list = sorted(citta)
print(x)
print(citta)

x : list = sorted(citta, reverse=True)
print(x)
print(citta)

citta.reverse()
print(citta)

favorite_places: dict = {"mauro":["roma", "venezia"], "paolo":["miami","losangeles"],"sfera":"newyork"}
print(favorite_places)