class Gym:
    def __init__(self,gender,opt_pt=False,duration=0):
        self.gender = gender
        self.opt_pt = opt_pt
        self.duration= duration

    def enrollment_to_personal_training(self,gym_fee,pt_fee):
        if self.duration == 12:
            gym_fee *= 0.9
        if self.opt_pt:
            enrolment_fee = (gym_fee * self.duration) + (self.duration * pt_fee)
            print(f"welcome to the Core fitness Gym! your {self.duration}-month fee is {enrolment_fee}")
        else:
            enrolment_fee = gym_fee * 2
            print(f"Your Gym fee per month is {enrolment_fee}")

pt= Gym("male",True,12)
pt.enrollment_to_personal_training(1000,3500)


pt1= Gym("female",False,0)
pt1.enrollment_to_personal_training(1000,0)




