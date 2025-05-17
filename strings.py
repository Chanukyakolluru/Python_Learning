#strings in python. [] represents the index value of the string, and always starts with zero.
# '-' negative represents the last character. start value and end value.
full_name='chanukya kolluru'
print(full_name[0:-8])

#formated strings to use 'f' as prefix where can be dynamically generate the output. syntax is f''
# if 2 or more string values to display

first_name='Chanukya'
last_name='Kolluru'
#print the message as Chanukya [Kolluru] wants to learn the Python programming.{} curley brackers are the
#place holders to hold the first and last names
message= first_name + ' [' + last_name + ']' + ' wants to learn the Python programming'
print(message)
msg=f'{first_name} [{last_name}] wants to learn the Python programming'
print(msg)

#string methods.
#len() is a general inbuilt function like as print. Not specific to string/int/float
# '.' (dot) represents to use the methods. ex: name.upper,name.lower to convert the lower case and upper cases
# find() and replace() methods usages in strings.find is case sensitive
# find syntax is find ('') and replace syntax is replace ('old value','new value')
# in operator/expression find the characters and if it matches gives True or Flase, where as find gives the index of the characets
name='Chanukya Kolluru'
print('The number of characters in ' + name + ' is ' + str(len(name)))
print(name.upper())
print(name.lower())
print(name.title())
print(name.find('k'))  # prints index as 5 for small k
print(name.find('K'))  # prints index as 9 for capital K
print(name.replace('Kolluru','Bharadwaj Kolluru')) # replaced name as Chanukya Bharadwaj Kolluru
print('Chanukya' in name) # gives True as Chanukya existed in the name variable, case sensitive

# strings are immutable , means once string created can't be changed.
# To get the address memory location of any variable use id()

str1 = 'chanukya'
print(id(str1))

str2 = 'Chanukya'
print(id(str2))

# String slicing- will fetch the some portion of the string
# syntax is : [start:end] . In between strings gets printed

str = 'Chanukya'
print(str[2:6]) # prints anuk (starts with index 2 and ends 6-1=5th value)

# ord() and chr ()
# ord returns the ASCII code of character
# chr returns the character of ASCII code

print(ord('A'))
print(chr(65))

#membership oerators or in and not in operators
# check the string existed in the other string and returns True or False

str = 'Chanukya Kolluru'
print("Chanukya" in str)   #True
print("bharadwaj" in str)  #False
print("kolluru" not in str)

# string comparison done with using the ASCII characters. letter to letter compare and then print

str1 = 'chanukya'
str2 = 'CHANUKYA'

print(str1.count('a'))  # prints the how many times a occured in the string. 2 times
print(str1 == str2)  # false

# converting strings

str = 'Chanukya bharadwaj Kolluru'
print(str.capitalize())  # only first character capitalized ("Chanukya bharadwaj kolluru)
print(str.title())   # every word first character capitalized ("Chankya Bharadwaj Kolluru)
print(str.lower())  # lower all the letters
print(str.upper())  # upper all the letters
print(str.swapcase()) # swap lower to upper and upper to lower
str = "   Chanukya "
print(str.strip())  #strip used to remove the spaces

str = "chanukya kolluru"
print(str.startswith("chanu"))
print(str.endswith("uru"))

# string to list conversion and vice versa
str = "Hey Chanukya How are you doing today"
print(str)
my_list = str.split()  #split used to convert string to list
print(my_list)
my_str = ' '.join(my_list)  # .join() method used to convert a list to string
print(my_str)

# .join() method is very effective when compared with list iteration to convert list to string
from timeit import default_timer
my_list = ["hey","chanukya"]
print(my_list)

start = default_timer()
my_string =''
for i in my_list:
    my_string +=i
stop = default_timer()
print(stop-start)   # takes 2.1999585442245007e-06
print(my_string)

start = default_timer()
my_list = ["hey","chanukya"]
my_string = ''.join(my_list)
stop = default_timer()
print(stop-start)   # takes 1.500011421740055e-06
print(my_string)

# string formating supports 3 ways
# older one - %, next - format(), finally f string

number = 6.2345
my_string ="my number is %d" % number # %d interpreter recognizes this formated as integer
my_string1 ="my number is %.2f" % number # %f interpreter recognizes this formated as float
print(my_string)
print(my_string1)

# second style- format
number = 6.2345
number1 = 5.67899
my_string = "variable is {:.2f} and {:.3f}".format(number,number1)
print(my_string)

# fstrings-
number = 6.2345
number1 = 5.67899
my_string = f"variable is {number*2} and {number1:.2f}" # using f string we can do runtime calculations as well
print(my_string)
