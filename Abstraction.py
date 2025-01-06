# Abstract class contains only method definition, but not the actual implementation
# want to secure our methods need abstraction
# when we know requirement and doesn't know impl, then use abstract class and later create subclass and implement
# Python supports the predefined abstract class as ABC , and @abstractmethod both should import from module abc
# Can't directly access the abstract method, to get access create a subclass (extends) and access
# subclass must implement all the methods defined in the abstract class, if not then subclass consider abstract class
# can create multiple subclasses for one abstract class

from abc import ABC, abstractmethod

class A(ABC):     # ABC denotes the Abstract class
    @abstractmethod  # @abstractmethod specifies that this method is abstract
    def display(self):
       pass           # No logic/implementation part

    def show(self):     # This is non-abstract method
        print('method is non abstract')

    @abstractmethod
    def visible(self):
        pass

class B(A):        # create a subclass to call the abstract class
    def display(self):  # implement the abstract method in the subclass
        print('This is an example of abstract method:')
    def visible(self):  # implement the abstract method in the subclass
        print('This is second abstract method:')


objb = B()
objb.display()  # access the abstract method
objb.show()     # access the non-abstract method
objb.visible()  # access the abstract method


# create a constructor in the abstract class along with 2 abstract methods

from abc import ABC, abstractmethod


class A(ABC):

    def __init__(self, value): # constructor for Abstract Class
        self.value = value

    @abstractmethod
    def sum(self):    # Abstract method just defined, no logic
        pass

    @abstractmethod
    def sub(self):
        pass


class B(A): # sub class created to access the Abstract class methods and varibales
    def sum(self):
        print(self.value+150)  # Actual abstract method implementation in the sub class

    def sub(self):
        print(self.value-100)


objectb = B(200)  # this step invokes the constructor , pass the argument
objectb.sum()
objectb.sub()