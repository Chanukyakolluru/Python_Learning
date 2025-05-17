#list : Ordered,mutable,Allow duplicates
#mutable-list elements can be altered/updated
# list unpacking
from math import sqrt

list1 = [1,2,3,4,5,6,6,7,8,9,11,14]

first,second,third,*rest =list1   # when numbers are more use *before so all the elements formed new list
print(first)
print(third)
print(rest)

print(list1[0:6])
print(list1[:])
print(list1[::2]) # this prints every other item in the list .1,3,5,6,8,11
print(list1[::-1])  # prints the list in reverse order

# create a list using range function

list2= list(range(21))
print(list2)   # this prints all the 20 items in the list

# enumarator object-

list =[1,2,4,5,8,11,13,14]

for index,item in enumerate(list):
    print(index,item)

# write a program to find the largest number in list

numbers = [12, 16, 86, 29, 3, 24, 26]
max_number = numbers[0]  # Assume the first item in the list as max number
for number in numbers:   # stores the value 12 at first
    if number > max_number: # compare 12 > 12 , not so reset the
        max_number = number # reset the max value
print(max_number)

# write a program to find the smallest number in list

numbers = [3, 45, 67, 2, 18]
min_number = numbers[0]
for number in numbers:
    if number < min_number:
        min_number = number
print (min_number)

# Two Dimensional lists

matrix = [
    [4, 6, 8],
    [1, 2, 5],
    [9, 7, 3]
]

for row in matrix:
    for i in row:
        print(i)

print(matrix[0][2])  # prints the value 8 here. [0] represents the entire first row, and then [2] represents the 8
print(matrix[2][2])  # prints 3
print(matrix[1][0])  # prints 1
print(matrix[1][1])  # prints 2

# list methods
# remove, insert, append, pop, clear, index,count,sort,reverse,copy

numbers = [2,23,55,12,78,43,67,55]
numbers[1] = 9  # update the value 23 to 9
numbers.append(33)  # append the value at the last
print(numbers)

numbers.insert(2, 99) # Insert the value using index place anywhere in the list (begining/middle))
print(numbers)

numbers.remove(43)
print(numbers) #removes the value 43 from the list

numbers.pop(1)
print(numbers)  #index is input, removes the value of that index place.

print(numbers.count(55)) # count is used to know the number of occurrence of that value

numbers.sort() # sort the values by ascending order
print(numbers)

numbers.reverse() # reverse the sorting order, basically descending order of the numbers
print(numbers)

# once value is append after copy, that doesn't impact the copied list. The 2 lists are independent each other.
numbers2 = numbers.copy()
print(numbers2)
numbers.append(77)
print(numbers)
print(numbers2)

numbers.clear()
print(numbers)   #clears the list

# write a program to remove the duplicates from the list
numbers = [2, 5, 2, 6, 5, 9, 8, 1, 2]
uniques = []
for i in numbers:
    if i not in uniques:
        uniques.append(i)
print(uniques)
#other way to remove duplictaes , convert the list to set-

numbers = [2,5,2,6,5,9,8,1,2]
new_numbers = set(numbers)
print('New list is:', new_numbers)
# list comprehension using for loop
# create a list with contains 25 numbers

list1 = [i for i in range(1, 26)]
print(list1)  # created the list with 25 numbers

# create a list with even numbers till 50

list2 = [i for i in range(1, 51) if i % 2 == 0]
print(list2)
#####################################################################

sports = ["cricket","tennis","basket ball","golf"]
movies = ["telugu","english","hindi","tamil"]
food =   ["vegetarian","non-vegetarian","vegan","eggtarien"]

collections = [["cricket","tennis","basket ball","golf"],
               ["telugu","english","hindi","tamil"],
               ["vegetarian","non-vegetarian","vegan","eggtarien"]]

for collection in collections:
    for food in collection:
        print(food,end=" ")
    print( )
###############################################
# create telephone number pad using tuple

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
######################################################
# list comprehension-
# syntax - [expression for value in iterable if condition]

double =[]

for x in range (1,11):
    double.append(x *2)
print("List after double the value:",double)

#################### using list comprehension write the above program#######

#double = [expression for value in iterable ]

double =[x*2 for x in range(1,11)]
print("List with comprehension:",double)

numbers =[x for x in range(1,40) if x%2 ==0]
print(numbers)

numbers = [pow(x,3) for x in range(1,10)]
print(numbers)

numbers = [round(sqrt(x),2) for x in range(1,10)]
print(numbers)

fruits = ["apple","Banana","orange","Mango"]
fruits = [fruit[0] for fruit in fruits]
print(fruits)

fruits = ["apple","Banana","orange","Mango"]
fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)
####################list copy#########################
list1_org = ["banana","apple","orange"]

list1_copy = list(list1_org)   # list() is a method
list1_copy.append("Cherry")
print(list1_copy)
print(list1_org)

list1_org = ["banana","apple","orange"]
list1_copy = list1_org.copy()  # copy() is method
list1_copy.append("blueberry")
print(list1_copy)
print(list1_org)

list1_org = ["banana","apple","orange"]
list1_copy = list1_org[:]  #slicing is another method
list1_copy.append("kiwi")
print(list1_copy)
print(list1_org)

list1_org = ["banana","apple","orange"]
list1_copy = [item for item in list1_org] #list comprehension best way
list1_copy.append("sapota")
print(list1_copy)
print(list1_org)
#####========================================================================
#covert a list to Tuple and vice versa

my_list = ["banana","apple","orange",24,1986]
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

my_list1 = list(my_tuple)
print(my_list1)
#################################
# Tuple unpacking
my_tuple= "chanukya",39,"killam"
name,age,city = my_tuple
print(name)
print(city)
print(age)
###############################
my_tuple = (1,2,3,4,5)
n1,*n2,n3 = my_tuple   # * represents for multiple elements, and n2 creates list as [2,3,4]
print(n1)
print(n3)
print(n2)
##################################################
#Tuples takes the less bytes when compared to lists

import sys

list1 = [1,3,"chanukya","anu",50]
tuple1 = (1,3,"chanukya","anu",50)

print(sys.getsizeof(list1),"bytes")   # list takes 104 bytes
print(sys.getsizeof(tuple1),"bytes")  # tuple takes 80 bytes

###########################
import timeit

print(timeit.timeit(stmt="[1,2,3,4,5,6]",number=10000000))
print(timeit.timeit(stmt="(1,2,3,4,5,6)",number=10000000))

#############sets################################################
#set: unordered,mutable,no duplicates
set1 ={1,2,3,4,5,6}
print(set1)

set2 =set(set1)  # set() function used
print(set2)

set3 = set1.copy()  # copy method to create
print(set3)

setA={1,2,3,4,5,6,7}
setB={1,2,6,8,9,11,13}

u = setA.union(setB)  # returns all items in both sets
print(u)

i= setA.intersection(setB) # returns common items in both sets
print(i)

d = setA.difference(setB) # returns only SetA remaining items
print(d)

e=setB.difference(setA)  # returns only SetB remaining items
print(e)

sd = setA.symmetric_difference(setB)  # returns all set A and SetB difference items
print(sd)

ud= setA.update(setB)  # returns setA which includes setB different items
print(ud)
