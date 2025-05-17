# To know the which version of python using
import sys
print(sys.version)

print('hello chanukya, welcome to Python learning')
#variable declaration
full_name='Chanukya Kolluru'
age= 38
is_henewtopython=True

#User Input receive. To concatenate the strings use the '+' symbol.'_' used to sepearate
#differentiate multiple words
#write a program to print person fav colour
name=input('what is your name? ')
favourite_colour=input('what is your favourite colour? ')
print('Hi, my name is ' + name + ' and my favourite colour is ' + favourite_colour)
# input fucntion is always returns the string value. We need to convert the string to integer or float values
#by using the int(),float() functions. type() is another built in function to know
#the whether it is string/int/float/boolean...

a = 10
print(a)
print(type(a))

a = 55
print(a)
print(type(a))

# Example for .format function to print the data

age = 38
name = 'Chanukya'
height = 5.11

print("Name: {} \nAge: {} \nHeight: {}" .format(name,age,height))
# print the values using the index number
print('print the values using index number:')
print("Name: {0} \nAge: {1} \nHeight: {2}" .format(name,age,height))
