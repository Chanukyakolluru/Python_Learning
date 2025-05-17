# Formula to calculate BMI = weight (kg) / height * height (meters)
class BMI:
    def __init__(self,name,height_mt,weight_kg):
        self.name = name
        self.height_mt = height_mt
        self.weight_kg = weight_kg
    def calculate_bmi(self):
        bmi = self.weight_kg/(self.height_mt * self.height_mt)
        print(f"{self.name}'s weight {self.weight_kg} kg's,and height {self.height_mt} meters, BMI is:{round(bmi,2)}")
        if bmi > 25:
            print("You are over weight!")
        elif bmi == 25:
            print("You are perfect weight!")
        else:
            print("You are just under weight!")

b = BMI("Chanukya",1.79,86.7)
b.calculate_bmi()


b1 = BMI("Anu",1,22)
b1.calculate_bmi()

b2 = BMI("Jyothi",1.65,55)
b2.calculate_bmi()