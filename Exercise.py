class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def display(self,color,mileage):
        print(f"The {color} car has {mileage:,} miles")


obj = Car('none',10)
obj.display('blue', 20000)
obj.display('red', 40000)

class Calculate:
    a = int(input('Enter number1:'))
    b = int(input('Enter number2:'))

    def mul(self):
        product = self.a * self.b
        return product


    def add(self):
        addition = self.a + self.b
        return addition

obj = Calculate()
print('Sum of numbers:',obj.add())
print('Multiple of numbers:',obj.mul())
####################################################################
var = 1000
a = int(input('Enter number1:'))
b = int(input('Enter number2:'))

sum = a+b
product = a*b

if product <= var:
    print (f'product of {a} and {b} is:', product)
else:
    print(f'sum of {a} and {b} is:', sum)
##########################################################################


def cal(self,x,y):
    product = x * y
    sum = x+y
if product<=1000:
    print('The product of numbers are:', product)
else:
    print('The sum of numbers are:', sum)
##==================================================================

class Vehicle:
    color = 'White'

    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


    def seating_capacity(self,capacity):
        return f"The seating capacity of {self.name} is {capacity} passengers:"


class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass


car = Car('Audi Q5',240,18)
print(car.color,car.name,car.max_speed,car.mileage)
bus = Bus("Volvo",180,12)
print(bus.color,bus.name,bus.max_speed,bus.mileage)
#print(bus.seating_capacity(50))
#print(f'vehicle details are:',bus.name, bus.max_speed, bus.mileage)
