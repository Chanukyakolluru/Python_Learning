class Person:  # person is a class name , Pasacal method, first lettershould be capital

    def __init__(self,name):  #init is a constructor automatically invoke when a new object created.name is the attribute
        self.name = name

    def talk(self):  # talk is a method and behavior of the class person.
        print("talk")


chanukya = Person("Chanukya Kolluru")  # chanukya is an obeject of the class person
print(chanukya.name)
chanukya.talk()  #Attributes and methods are accessed using the dot (.) operator.


# Class contains Data(properties/variables) and Functions(Methods).
# These Data and functions are called as Class members.
# To access the Class members , we need to create Object.
# So Object is a reference of class to access the class members.
# Single class can have multiple objects.
# Two kind of variables defined in Class-Instance variables and Local Variables
# Instance/global variables are defined within the class but outside the function.
# Local variables are defined within the function.
# When there are same variables , always local variables takes precedence over instance variables
# To get access the instance variable within the function/method, call them as (self.instance variable)
# self is a implicit instance of a class
# Write a program Student as class. Roll Number,Name,Gender and Age as Data.
# Create two methods as read() and write()

class Student:
    roll_number = 47418  # this is instance variable
    name = 'Chanukya Kolluru'
    age = 38
    gender = 'Male'

    def read(self):
        roll_number = 389450  # this is a local variable
        print('student roll number is: ', roll_number)
        print('student instance roll number is:',self.roll_number)  #using self accessing the instance variable in method
        print('student can read')

    def write(self):
        print('student can write')


student1 = Student()  # Create an object - student1 to access all class data and methods
#print('student roll number is:', student1.roll_number)
print('student name is :', student1.name)
print('student gender is:', student1.gender)
print('student age is:', student1.age)

student1.read()  # access the clss methods
student1.write()


#Write a Python program to create a person class. Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.

class Person:

    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        age = 2024 - int(self.dob)
        return age
        print(f'person age is :', age)


person1 = Person('Chanukya', 'India', '1986')
person2 = Person('Bharath', 'India', '1985')
person3 = Person('Goutami', 'India', '1984')

print(person1.calculate_age())
print(person2.name)


# Instance method and Static Method.
# Static method can labeled as @staticmethod and it called by with the class itself, no need of object
# Also static method doesn't require any param to pass , not even self

class InstanceStatic:
    def Instance_method(self):
        print('This is Instance method')

    @staticmethod
    def Static_method():
        print('This is static method')


ism = InstanceStatic()
ism.Instance_method()
ism.Static_method()
InstanceStatic.Static_method()  # can call directly with the help of Class itself

# Local variables, Class Variables and Global variables
# Local variable-variable declared within the Method is called. And access through the object
# Class variable-variable declared within the Class is called. And access through 'self'
# Global variable-variable declared outside the class is called.

x, y = 10, 20  # global variables
class DifVariables:
    a, b = 25, 35  # class variables

    def add(self, p, q):  # local variables, within the method declared
        c = self.a + self.b
        z = x + y
        print('The sum of local variables :', p + q)
        print('The sum of class variables :', c)
        print('The sum of global variables :', z)


variables = DifVariables()
variables.add(50, 60)

# If the local, class and global variables are with the same names
# To access global variables use - globals()['variable']

a,b = 55, 65
class AddTwoNumbers:
    a,b = 20,40
    def add(self,a,b):
        print('The sum of local variables:', a+b)
        print('The sum of class variables:', self.a+self.b)
        print('The sum of global variables:', globals()['a']+globals()['b'])

atn=AddTwoNumbers()
atn.add(30,35)

# convert the class variables to local variables by specifying - 'self.variable'

class Variable:
    def display(self,a,b):     # local varibales, within the method defined
        print(a)
        print(b)
        self.a = a             # using self.a converting local variable to Class variable
        self.b = b
    def sum(self):
        print(self.a+self.b)
v=Variable()
v.display(10,20)
v.sum()

# check memory locations of objects using id() and also check with 'is' and 'is not'
class MemoryLocations:
    def method1(self):
        print('check the memory of object')


ml = MemoryLocations()
print(id(ml))                           #2760829137792

ml2 = MemoryLocations()
print(id(ml2))                          #2760829137888

ml3 = ml                                #2760829137792
print(id(ml3))

print(ml is ml2)    #Flase, the memory location is not same
print (ml is ml3)   #True
print(ml is not ml3) #False

#create a constructor. constructor can be created using __init__
# constructor with arguments/values
#varibales which passed to constructor considered as local variables only.

class Constructor:
    def method(self):
        print('this is a method inside of the class:')
    def __init__(self):
        print('this is a construtor created using init method and as soon as object created this is invoked automatically')


c=Constructor()
c.method()

class ArgumentConstructor:
    name='Bharath'          # class variable
    def __init__(self,name): # name is local variable
        print(name)
        print(self.name)     # self.name is class variable, and so this prints 'Bharath'
ac=ArgumentConstructor('Chanukya')


# call a method from another method within the same class.

class MethodCall:
    def method1(self):
        print('this is method1 in the class:')
        self.method2(120,125)      # by using self.method2 calling this method2 from method1 itself
    def method2(self,c,d):
        print('this is method2 in the class to sum the numbers:', c+d)
mc=MethodCall()
mc.method1()

# create an emp class and display empid,name and salary

class Employee:

    def __init__(self,empid,name,salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    def display(self):
        print('display the employee attributes:')
        print('Employee id is: ', self.empid)
        print('Employee name is: ', self.name)
        print('Employee salary is:', self.salary)
        print('Display the Employee attributes-\nid:{},name:{},salary:{}'.format(self.empid,self.name,self.salary))
emp = Employee(1,'chanukya',35000)
emp.display()

# __str__ method. Whenever the reference object printed, str method invokes.
# must return the values in __str__ method
# ideally str returns the memory of that object if we not define any return inside the method
# __del__ destroys the object
class Employee:

    def __init__(self,empid,name,salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def __str__(self):
            return('Display the Employee attributes-\nid:{},name:{},salary:{}'.format(self.empid, self.name, self.salary))

emp = Employee(1, 'chanukya', 35000)
print(emp)  # as soon as printing the emp which is reference object of class, invokes the __str__ method
#############

class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    def display(self,color,mileage):
        return f"The {self.color} car has {self.mileage} miles"
obj = Car('green',35000)
obj.display('blue',20000)
obj.display('red',30000)

class University:

    def __init(self):
        pass
    def sports(self):
        print('This is the university to play the sports')

class College(University):

    def play(self):
        print('This is the college to play the games')

    def study(self):
        print('Boys to study well')

class School(College):
    def study(self):
        print('Children to study well')

sch = School()
sch.study()
sch.sports()
sch.play()

#######################################



