
from datetime import datetime
class CalAge():
    def __init__(self,name,gender,dob):
        self.name = name
        self.gender = gender
        self.dob = dob

    def personage(self):
        current_year = datetime.now().year
        age = (current_year - self.dob)
        if age >=18:
            print(f"Hey {self.name}, you are {age} year's old and eligible to vote!")
        else:
            print(f"Hey, {self.name} you are kid, you are just {age} year's old and have time to vote!")

page =CalAge("Chanukya","Male",1986)
page.personage()

page1 = CalAge("Anu","Female",2016)
page1.personage()

