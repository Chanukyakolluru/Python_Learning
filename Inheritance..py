# Inheritance acquiring the properties from the Parent class/Base Class.
# No need to create an object for the Base class, object can create for derived class and
# can access Base class members (data/attributes and functions/methods)
# 3 types of Inheritances- Single ( 1parent and 1 child), multi-level
# and multiple inheritance (2 parents and 1 child)

class GrandParent:
    def eat(self):
        print('Grand Parent retired and takes the rest at home and eat well!')
class Parent(GrandParent):
    def works(self):
        print('Parent works hard to feed the family!')

class Child(Parent):
    def enjoy(self):
        print('Child enjoys the childhood and go the school')


child1 = Child()

child1.enjoy()
child1.works()
child1.eat()

# write a program on multi level inheritance

class Vehicle:
    def diesel(self):
        print('Vehicle consumes diesel to run')

class PetrolVehicle(Vehicle):
    def petrol(self):
        print('vehicle consumes the petrol to run!')


class HybridVehicle(PetrolVehicle):
    def hybrid(self):
        print('vehicle consumes the petrol and electric to run!')


vehicle1 = HybridVehicle()

vehicle1.hybrid()
vehicle1.petrol()
vehicle1.diesel()

#==================

# write an example for multiple inheritance

class A:
    def function1(self):
        print('function1 belongs to class A')

class B:
    def function2(self):
        print('function2 belongs to class B')

class C(A,B):                    #multiple inheritance both the class A and class B inherited here.
    def function3(self):
        print('function3 belongs to class C')


c1 = C()
c1.function3()
c1.function1()
c1.function2()

#========================================================================

# constructor example-
# super() method will be used to invoke  the parent Class method within the Child class
# - used to invoke the parent class method
# - used to invoke the parent class variables
# - used to invoke the parent class constructor

class A:
    def __init__(self):
        print('this is the init method for class A')
    def function1(self):
        print('function1 belongs to class A')

class B(A):
    def __init__(self):
        super().__init__()                    # this will call the class A init method with class B object
        print('this is init method for class B')
    def function2(self):
        print('function2 belongs to class B')


b1 = B()                   # this is initiated only the class B init method not class A init method.To access classA init
# need to define the super().__init method in class B.
b1.function2()
b1.function1()
#==================================================================

# MRO- Method Resolution order. Always follows left to Write order of the classes/methods defined.

class A:
    def function1(self):
        print('Function1 belongs to class A')

class B:
    def function2(self):
        print('Function2 belongs to class B')

class C(A,B):

    def __init__(self):
        print('This is init method for class C')
    def function3(self):
        super().__init__()
        super().function2()
        print('Function3 belongs to class C')


c1 = C()
c1.function3()     #here this function1 calls the method from Class A not from Class B (left to right)

# write a program to access super class variables, class variables and local variables,global with different variables

c,d = 12 ,17
class A:
    a,b = 10, 20     # Parent class variables
class B(A):
    x, y = 50, 70    # child class variables
    def add(self,i,j):  # local variables
        print('The sum of local variables:', i+j)
        print('The sum of child class B variables:',self.x+self.y)
        print('the sum of Parent Class A variables:', self.a+self.b)
        print('the sum of global variables :', globals()['c']+globals()['d'])
objectb = B()
objectb.add(90,190)

# write a program to access super class variables, class variables and local variables,global with SAME variables

a,b = 10, 20   # global variables
class A:
    a, b = 30, 40  # parent class variables
class B(A):
    a, b = 50, 60  # child class variables
    def sum(self,a,b): # local variables
        print('sum of local:', a+b)
        print('sum of child class B:', self.a+self.b)
        print('sum of parent class A:', super().a+super().b)   # super().variable used to invoke parent class variable
        print('sum of global:',globals()['a']+globals()['b'])  # globals()['variable'] to invoke global variable
objb = B()
objb.sum(70,80)

# Invoke parent class constructor- two approaches existed
# 1) user super().__init__
# 2) call from parent class name

class A:
    def __init__(self):
        print('This is parent class A constructor')
class B(A):
    def __init__(self):
        print('This is child class B constructor')
        super().__init__()  # this will invoke the parent class A constructor (approach1)
        A.__init__(self)      # approach2 invoke by parent class name with self as argument
objb= B()

#######################################################################################
class Add:
    a, b = 50, 60
    def add(self,a,b):
        result = a+b
        print(f'sum of {a} and {b} is:',result)
class Sub(Add):
    a, b = 40, 80
    def sub(self,a,b):
        res = a-b
        print(f'subtraction of values {a} and {b} is:',res)
class Mul(Sub):
    a, b = 10, 20
    def __init__(self):
        self.a = a
        self.b = b
        rslt = a*b
        print(f'Multiplication of {a} and {b} is:', rslt)
        super().add(super().a,super().b)
        self.sub(super().a,super().b)

obj=Mul()
obj.add(a,b)

