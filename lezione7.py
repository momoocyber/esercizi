# Write a function to find all numbers divisible by 7,
# not a multiple of 5, between 2000 and 3200 (both included). 
# The numbers should be stored in a list and returned as output.



def numbers():
    result = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            result.append(i)
    return result


numeri = numbers()
print(numeri)



# Write a function to calculate the factorial of a number 
# given as input. The number should be returned as output.
# For example:

#    Input: 8
#    Output: 40320


def facto(number : int):
    factorial=1
    i= number
    while i>0 :

        factorial = factorial * i 

        i= i-1

    return factorial

   
fattoriale= facto(8)
print(fattoriale)



# Use the function implemented in Exercise 2 to compute all factorial
#  numbers of a list of numbers. The list is given as input to the function.
# All factorials should be returned as output. For example:

#    Input: [2, 5, 8, 10]
#    Output: [2, 120, 40320, 3628800]


def list_factorials(numbers: list):
    factorials = []
    for i in numbers:
        factorials.append(facto(i))
    return factorials


fatto=list_factorials([2,5, 8, 10])

print(fatto)



# Given an integer n as input, write a function to generate a dictionary 
# that contains (i, i*i) as (key, value) pairs such that i is an integer 
# between 1 and n (both included). The function should return the dictionary
# as output. For example:

#    Input: 8
#    Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


