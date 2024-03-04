class father:

    def home(self):
        print("Father's Home")

    def money(self):
        print("Father's Money")

class mother:

    def Home(self):
        print("Mother's Home")

    def Money(self):
        print("Mother's Money")

class son(father, mother):
    pass

pramod = son()
pramod.Home()
pramod.home()
print("--------------")
pramod.money()
pramod.Money()