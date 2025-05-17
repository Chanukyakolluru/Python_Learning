class CalBonus():
    def __init__(self,annualsalary,maxbonus,totalbonus):
        self.annualsalary = annualsalary
        self.maxbonus = maxbonus
        self.totalbonus = totalbonus
    def groupbonus(self,taxpercentage = 30):
        bonus_amount = (self.annualsalary * self.maxbonus/100)
        beforetax_bonus_to_paid = (bonus_amount * self.totalbonus/100)
        print(f"Before Tax Bonus:{round(beforetax_bonus_to_paid,2)}")
        aftertax_bonus_to_paid = beforetax_bonus_to_paid-(beforetax_bonus_to_paid * taxpercentage/100)
        print(f"After Tax Bonus Amount : {round(aftertax_bonus_to_paid,2)}")

bonuscal = CalBonus(2184004.20,15,93.6)
bonuscal.groupbonus()