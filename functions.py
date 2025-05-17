# function contains the piece of code and can be reusable whenever that calls. def is the keyword

def greet_user():
    print('Hi, I am Chanukya Kolluru')
    print('I am learning the python coding')


print('call the function to print the statements defined in the function')
greet_user()
print('end of the function')

#funciton with sinlge parameter as input.
#parameters are the placeholders/postions where as arguments are actual values we are passing to that parameters
# define the funciton first and then callout the function.
def greet_user(name):
    print(f'Hi, {name}')
    print("How are you doing today ?")

print('starts the function')
greet_user("Bharath")
greet_user("Goutami")
print('end of the function')

# function with multiple parameters as an example.
# we need to supply the values for the parameters

def hello_user(first_name,last_name,age):
    print(f'first name is:{first_name}')
    print(f'last name is:{last_name}')
    print(f'age is:{age}')
    print("How are you doing today ?")


print('call the function')

hello_user("Chanukya","Kolluru",38)
hello_user("Bharath","Kolluru",39)
hello_user("Goutami","Kolluru",40)
hello_user("Jyothirmayi","Chittella",34)
print('function ends here !')


# we have two types of parameters. can improve the readability of code by reading what values are assigned
# 1) positional parameters and 2) keyword parameters ( not required any position)
# Always add a keyword argument after the positional argument only
# use the keyword arguments only when dealing functions with numeric values to more specific and clear
def hi_user(first_name,last_name):
    print(f'first name is:{first_name}')
    print(f'last name is:{last_name}')
    print("How are you doing today ?")


print('call the function')
hi_user(last_name='kolluru',first_name='Chanukya') # no mater the order of the posiiton
hi_user('Bharath',last_name='kolluru') # here first positional parameter and followed by keyword argument
print('end of the function')

# return function. By default all the functions in python return 'None'

def square(number):
     return number * number

result = square(3)
print(result)
print(square(3)) # directly write the function within the print statement

# write a function to sum up the 2 numbers


def sum_numbers(number1, number2):
    return num1+num2


num1 = int(input('Enter the number1: '))
num2 = int(input('Enter the number2: '))
result = sum_numbers(number1=num1, number2=num2)   # calling the function
print('sum of the two numbers are :',  result)

##################################################

def create_fullname(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

name = create_fullname("chanukya","kolluru")
name1 = create_fullname("bharath","kolluru")
name2 = create_fullname("gouthami","kolluru")

print(name,name1,name2)

#############################
# time counter program

import time

def counter(end,start=0):
    for i in range(start,end+1):
        print(i)
        time.sleep(0.5)
    print("Done!")


counter(10)
counter(20,11)





