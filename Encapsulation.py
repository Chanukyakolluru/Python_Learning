# Encapsulation- restrict the variables and methods to access
# prefix '__' before the variable/ method to denote the private and restrict access
# private variables can only access within the class, can't access outside the class.

class A:
    __a = 10 # private variable
    def disply(self):
        print(self.__a)   # to access class variable use self. and access private variable use __
objecta1 = A()
objecta1.disply()
#print(A.__a) # we can't access private variable outside the class

# private methods - can't access outside of the class

class A:
    def __display(self):
        print('this is private method of class A')
    def show(self):
        print('this is public method of class A')
        self.__display()   # using self.__(class name) calling the private method here
objecta1= A()
objecta1.show()
#objecta1.__display()  # can't access the private method display, outside of class A
# can modify the private variables outside class indirectly by using methods

# Though inheritance we can;t access the private method of the class from another class.
class X:
    def __display(self):
        print('Display is the private method of class X:')
class Y(X):
    def show(self):
        print('show is the method of class Y:')
        self.__display()


obj = Y()
obj.show()
class A:
    __a = 15

    def getvalue(self,a):
        self.__a = a
    def display(self):
        print(self.__a)
objb= A()
objb.getvalue(35)
objb.display()