class ProvidentFund:
    def __init__(self,basic_salary,pf_percent,vpf_percent):
        self.basic_salary = basic_salary
        self.pf_percent = pf_percent
        self.vpf_percent = vpf_percent

    def calculate_pf(self):
        employee_contribution = self.basic_salary * (self.pf_percent / 100)
        vpf_contribution = self.basic_salary *(self.vpf_percent/100)
        monthly_pf_balance = employee_contribution + vpf_contribution
        yearly_pf_balance = (monthly_pf_balance * 12)
        print("#####Here the Breakdown#####")
        print(f"Monthly PF balance:{monthly_pf_balance:.2f}")
        print(f"Yearly PF balance:{yearly_pf_balance:.2f}")
        print(f"PF Contribution:{self.pf_percent:.2f}")
        print(f"VPF Contribution:{self.vpf_percent:.2f}")
    def __str__(self):
        return(f"provident fund(basic salary is:{self.basic_salary},"
               f"pf_percent={self.pf_percent}%, vpf_percent={self.vpf_percent}%)")

pf = ProvidentFund(97400,12,2)
pf.calculate_pf()

pf = ProvidentFund(91000,12,2)
pf.calculate_pf()

