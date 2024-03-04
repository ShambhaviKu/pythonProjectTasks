class Loan:

    def __init__(self, duration, principal):
        self.duration = duration
        self.principal = principal

class homeloan(Loan):

    def cal_home_loan(self, intrest):
        if self.duration > 0 and self.principal > 100000:
            print((self.principal * self.duration * intrest) / 100)
            print("eligible for loan")
        else:
            print("not eligible for loan")

class carloan(Loan):

    def cal_car_loan(self, intrest):
        if self.duration > 0 and self.principal > 100000:
            print((self.principal * self.duration * intrest) / 100)
            print("eligible for loan")
        else:
            print("not eligible for loan")



home1 = homeloan(0, 1000)
home1.cal_home_loan(9)

car1 = carloan(10, 200000)
car1.cal_car_loan(10)
