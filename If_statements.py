#write a program to print the message based on weekday or weekend
is_weekday=False
is_weekend=True

if is_weekday:
    print("It's a working day")
    print("Go to the office and get the tasks done!")
elif is_weekend:
    print("It's not a working day")
    print("Go the grocery store and get the home needs")
else:
    print("It is Holiday!")
print('Enjoy your day!')

# Grade of the student and print the message

maths=int(input('Enter the marks :'))
physics=int(input('Enter the marks :'))
chemistry=int(input('Enter the marks :'))

total=maths+physics+chemistry
average=(int(total)//3)

if (average>70):
    print('Student scored the merit marks and got the grade A ' + str(average))
elif (average>=35 and average<=70):
    print("Student didn't score the merit marks and got the grade B" + str(average))
else:
    print('Student failed and work hard to pass')

##########using function ######################

class Grade:
    def __init__(self, maths, science, english):
        self.maths = maths
        self.science = science
        self.english = english

    def total_marks(self):
        total = (self.maths + self.science + self.english)
        average = (total / 3)
        print(round(average,2))
        if average >= 75:
            print(f"Student passed with A grade:")
        elif average < 75 and average > 60:
            print(f"Student passed with B grade:")
        elif average >= 35 and average <= 60:
            print(f"Student passed with C grade:")
        else:
            print(f"Student failed!")

grd = Grade(90, 80, 55)
grd.total_marks()

grd1 = Grade(90, 70, 55)
grd1.total_marks()

grd2 = Grade(60, 60, 55)
grd2.total_marks()

grd3 = Grade(25, 35, 30)
grd3.total_marks()


#write a program to discount the price of house based on buyer's credit history.

house_price = 1000000
has_good_credit = False
has_bad_credit = True

if(has_good_credit):
    down_payment = 0.1*house_price
    print(f"Buyer to do the down payment of 10%, the value is :${down_payment}")
elif(has_bad_credit):
    down_payment = 0.2*house_price
    print(f"Buyer to do the down payment of 20%, the value is :${down_payment}")
else:
    print("Buyer can't effort the house to buy at this moment")

#logical operators-AND, OR , NOT

has_high_income = True
has_good_credit = False

if has_high_income and not has_good_credit:
    print('eligible for loan!')
else:
    print('not eligible for loan')

#comparision oeprators. compare the varibale with value.
# >,>=,<,<=,==,!=
#write a program to asses the name characters greater the 4 and less the 10 characters and print message

name = input('Enter the name :')
if len(name) < 4:
    print("please enter the minimum 4 character's")
elif len(name) >= 4 and len(name) <=9:
    print("Entered name is valid to fill the form")
else:
    print("maximum characters limit exceeded!")

# print the weight of the person in kilos and pounds
# 1 kilo= 2.20 pounds
weight = int(input('enter the weight: '))
unit = input("weight in kilo's (k) or lb's(l)")

if unit.upper == 'L':
    convert_weight = weight * 2.2
    print(f"you are weight is {convert_weight} in kilo's")
else:
    convert_weight = weight / 2.2
    print(f"you are weight is {convert_weight} in pound's")

# print the number is even or odd using if else

num = int(input('enter the number:'))
print('Number is Even:', num) if num % 2 == 0 else print('Number is Odd:', num)



