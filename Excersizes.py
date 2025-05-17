# calculate the Area of Rectangle Area = Length * Width

length = float(input("Enter the length:"))
width = float(input("Enter the width:"))

area = length * width
print(f"The Area of Rectangle is:{area} with the length {length} and width {width}")

# Shopping cart with Number of Items, Price and calculate Total cost

item = input("What would you like to buy ?")
price = float(input("How much cost it is ?"))
quantity = int(input("How many number of items you want?"))

total_cost = price * quantity
print(f"You have purchased {quantity} {item} and the cost of {item} are:{total_cost} INR")

# calculate the circumference of circle - c = 2pir
# To get the pi value import the math module
# round function with digits restrict the float decimals

import math
radius = float(input("Enter the radius of circle:"))
circumference = 2 * math.pi * radius

print(f"The radius of circle is {radius} and the circumference of circle is: {round(circumference,2)}")

#calculate the area of the circle - pi r*r
#power function used to calculate

import math
radius = float(input("Enter the radius of circle:"))
#area = math.pi*radius*radius
area = math.pi * pow(radius,2)
print(f"The radius of circle is {radius} and the area of circle is:{round(area,3)}")

#calculate the side C of Right angle traiangle c = sqrt of a^2 + b^2
import math
a = float(input("Enter the side of A:"))
b = float(input("Enter the side of B:"))
c = math.sqrt(pow(a,2)+pow(b,2))
print(f"The square root of side c is:{round(c,2)}")

#check the user can vote or not based on age using if else conditions

age = int(input("Enter your age:"))

if age<=0:
    print("Age shouldn't be negative or zero, you must enter the age greater than zero")
elif age>0 and age<17:
    print("You are too young to vote!")
elif age>=18 and age<=80:
    print("You are eligible to vote")
else:
    print("You are too old, and so you can't vote")

# Based on user's response watch the movie tonight !

watch_movie = input("Shall we go to movie tonight ? (Y/N):")

if watch_movie == "Y":
    print("we will go to movie tonight")
else:
    print("No movie to watch!")

# check the number is even or odd and print

number = int(input("Enter the number:"))

if number < 0:
    print("please enter the positive number")
elif number %2 ==0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")

# Weight convertor

weight = float(input("Enter the weight: "))
unit = input("weight unit in kgs/lbs (K/L): ")

if unit == "K":
    weight = weight * 2.204
    unit = "lbs"
    print(f"The weight is {round(weight,2)} {unit}")
elif unit == "L":
    weight = weight / 2.204
    unit = "kgs"
    print(f"The weight is {round(weight,2)} {unit}")
else:
    print("enter the weight input properly")

##############################
# conditional expressions- X if condition else Y
# positive or negative number
number = 5
result = "positive" if number >0 else "negative"
print(result)
###########################################
user_name = input("Enter your full name: ")

if len(user_name) > 12:
    print("user name must be within the 12 characters")
elif not user_name.find(" ") == -1:
    print("user name can't have the spaces")
elif user_name.isalnum():
    print("User name can't have digits")
else:
    print(f"Welcome {user_name}")
################################################
#print the last 4 digits of the credit card

card_number = "5557-5678-9012-3456"
last_digits = card_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

#Reverse the card details

card_number = "5557-5678-9012-3456"
new_card = card_number[::-1]
print(f"The new card after the digits reversed is: {new_card}")

# format specifiers

price = 30000.1234
print(f"price is:{price:+,.2f}")

### while loops

number = int(input("enter the numbers between 1 to 10: "))

while number < 0 or number > 10:
    print(f"The number {number} is not valid")
    number = input("enter the numbers between 1 to 10: ")

print(f"The number is : {number}")

fav_food = input("Enter your favourite food: ")

while not fav_food == "q":
    print("quit the app")
    fav_food = input("Enter your another favourite food: ")

print ("bye")



