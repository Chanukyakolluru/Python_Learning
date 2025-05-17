# Argument is an input which is passed to a function
# 4 types of arguments existed
#  1)Required arguments (Positional Arguments) -At function definition and function call number of arguments should be same
#                       position/order should be followed

def show(a, b):
    print(a, b)


show(30, 50)  # as per position a and b values are assigned. a=30 and b=50
show(50, 30)  # a=50 and b=30

#Keyword arguments- No position required to display
#                   mapping will be done based on the keywords (a and b are the keywords here)

def show(a, b):
    print(a, b)

show(b = 30, a = 50)

#Default arguments- some of the arguments consider as default arguments
#                   Number of arguments need not to match in function definition and on function call
#                   If argument not called in the function call, argument value considered from function definition

def show(name,age=38):
    print(name)
    print(age)

show('Chanukya')
show('Akka', age = 42)
show('Bharath', 39)

# Arbitary Arguments (variable length arguments)- when user doesn't know how many arguments passed at function call
#                          - use "*" as prefix before the argument in the function definition

def show(* courses):      # * used as prefix here
    for item in courses:
        print(item)


show("MBA", "MCA", "B.Tech", "M.Tech")   # passed all the 4 courses but defined only one attribute 'courses'


def display(x,y):
    print('These are the arguments:',x,y)

display(70,80)   # Required Arguments
display(y=55,x=45)     # Keyword Arguments


def show(name,age=38):
    print('My name is',name,'and I am',age,'Old')

show('Chanukya') # Default Argument.Age from the function definition considered, since it is not called out
show( age = 42,name ='Gouthami')  # Keyword Arguments
show('Bharath', 39)    # Required Arguments

def show(*name):
    print('display all the user names:', name)

show('viri','chani','bharath','keerti','sai') # more names passed at calling * defined to indicate variable length

############## Shipping address using *args and **kwargs

def shipping_address(*args,**kwargs):
    for arg in args:
        print(arg, end =" ")
    print()
    for key,value in kwargs.items():
        print(f"{key}:{value}")


shipping_address("Mr.","Chanukya","Kolluru",
                 flat_no="204",
                 Apartment="Srinivasam New Block",
                 landmark= "Besides vertex villas",
                 Area="Nizampet",
                 State="Telangana",
                 phone =9581507786)
