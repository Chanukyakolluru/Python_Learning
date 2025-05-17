for items in 'Chanukya':
    print(items)

for items in ['Chanukya','Bharadwaj','Kolluru']:
    print(items)
for items in [1,2,3,4,5,6,7]:
    print(items)
for items in range(10):
    print(items)
#range is a built in function.
for items in range(1,10,3):   # start, stop, end (difference)
    print(items)   # prints 1,4,7. Starts with 1, step as 3, and ends within 10)

#write a program to calculate the list of items in collection. Sum all the items

prices = [10,20,40]
sum = 0
for price in prices:
    sum = sum+price
print(f"sum of the price is: {sum}")

#Nested Loops. loop in a loop is called nested, usually used to create the coordinates

for x in range(3):
    for y in range(2):
        print(f'({x},{y})')
#*****
#**
#*****
#**
#**

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    outcome = ''
    for y in range(x):
        outcome += 'x'
    print(outcome)

# try to print L
# **
# **
# **
# **
# ******

numbers = [2, 2, 2, 2, 6]

for a in numbers:
    a_count = ''
    for b in range(a):
        a_count += 'x'
    print(a_count)

#########################
# break and continue statements examples

for i in range(1,11):
    if i == 7:
        break          # this will stop the printing once i value reached to 7, so print the numbers till 6.
    print(i)

for i in range(1,11):
    if i == 7:
        continue       # this will exclude the number 7 and continue to print the next values
    print(i)

####

for i in range(10):
    print('Welcome to New Year 2025')

