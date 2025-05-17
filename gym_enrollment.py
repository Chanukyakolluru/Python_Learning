class Gym:
    def __init__(self,name,member_id,gender):
        self.name = name
        self.member_id = member_id
        self.gender = gender
    def get_enroll(self):
        if self.gender == "male":
            print(f"Hey Mr.{self.name}, welcome to Core fitness Gym!")
        elif self.gender == "female":
            print(f"Hey Ms.{self.name}, welcome to Core fitness Gym!")
        else:
            print("Invalid gender passed!")
    def opt_personaltraining(self,enroll_months):
        if self.gender == "male":
            gym_fee_permonth = 1000
        else:
            gym_fee_permonth = 700
        ptfee_permonth = 3000
        amount_to_paid = (gym_fee_permonth * enroll_months) + ptfee_permonth
        print(f"Your gym fee for {enroll_months} months : gym fee {gym_fee_permonth*enroll_months} and PT {ptfee_permonth} :{amount_to_paid} INR")

enroll_months = int(input("Enter the number of months for PT: 1 or 3 or 6 or 9 or 12: "))

gym = Gym("Chanukya",1001,"male")
gym.get_enroll()
gym.opt_personaltraining(enroll_months)

gym1 = Gym("Jyothi",1002,"female")
gym1.get_enroll()
gym1.opt_personaltraining(enroll_months)