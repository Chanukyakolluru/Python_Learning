#polymorphisam is same method implement in different ways.
# 2 Types- overloading and overiding
# further overloading as 2 types-operator overloading and method overloading
# '+' is an example for operator overloading. strings used as "concatenate" and for integers used as "addition"
# Method overloading is - single method and passing different variables
#Write a program for method overloading

class MethodOverload:
    def add(self, a, b):
        print('The sum is: ', a+b)


methodobject = MethodOverload()

methodobject.add(20,30)
methodobject.add(10,20)
methodobject.add(25,35)

#overiding- override the base class method in the derived class. Use the inheritance concept here
# conditions- 1)method name should be same in both base and derived class
#             2)number of attributes,type of attributes should be same in both base and derived class.
# write a program for method overriding.

class Dad:
    def study(self):
        print('Dad studied at govt school')


class Daughter(Dad):
    def study(self):
        print('Daughter studying at DPS Miyapur, private school')

objdaughter = Daughter()
objdaughter.study()

# variable overriding example

class A:
    name='Chanukya'
class B(A):
    name='Kolluru'
objectb = B()
print(objectb.name)  # overirde the name and prints kolluru
print('This will print the Base class variable name:',A.name)

class A:
    name='Chanukya'
class B(A):
    pass

objectb = B()
print(objectb.name)  # prints chanukya, as in class B we passed and nothing to override

# overriding methods

class A:
    def display(self):
        print ('this is display of class A')
class B(A):
    def display(self):
        print('this is display method of class B:')
obj = B()
obj.display()  # this will prints -'this is display method of class B:'


