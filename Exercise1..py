class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

obj = Person('Chanukya', 38)
obj.greet()

obj1 = Person('Bharath', 39)
obj1.greet()

obj2 = Person('Gouthami', 40)
obj2.greet()

###########################################################
class Animal:
    def make_sound(self):
        print("some generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")



class Cat(Animal):
    def make_sound(self):
        print("Meow!")
        super().make_sound()


objd = Dog()
objd.make_sound()
objc = Cat()
objc.make_sound()

############################################################


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f'amount deposited is:{amount}')

        else:

            print('Invalid deposit amount')

    def withdraw(self,amount):

        if amount > self.__balance:
            print('Insufficient balance')
        elif amount > 0:
            self.__balance -=amount
            print(f'Withdraw amount is:,{amount}')
        else:
            print('Invalid withdraw amount')
    def get_balance(self):
        return self.__balance

amt = BankAccount()
amt.deposit(1000)
amt.deposit(1500)

amt.withdraw(1000)
amt.withdraw(2000)
print("Current balance is :", amt.get_balance())


########################################################
import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius **2)


rect = Rectangle(10,20)
cir = Circle(10)

print(f'Area of Rectangle is:{rect.area()}')
print(f'Area of Circle is:{cir.area()}')
#==============================================================

p, q = 90, 100
class A:
    x,y = 10,30
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print('sum of local variables:',self.a+self.b)
        print('sum of instance variables:',self.x+self.y)
        print('sum of global variables:', globals()['p']+globals()['q'])
        print('sum of global variables:', p+q)

class B(A):

    def sub(self,c,d):
        print('difference of local variables:',c-d)
        print('difference of Base class variables:',self.x-self.y)
        print('sub of global variables:', globals()['p']-globals()['q'])
        print('sub of global variables:', p-q)


objb= B(55,65)
objb.add()
objb.sub(40,50)









