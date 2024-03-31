class Father:
    __private_villa = "Pune"
    Gold = 5

    def driveCar(self):
        print("lamb")

    def ownFlat(self):
        print("3BHK Flat")

    def auth(self, is_son):
        if is_son:
            print(self.__private_villa)
        else:
            print("NA")


class son(Father):
    pass


pramod = son()

print(pramod.Gold)
pramod.auth(True)
pramod.ownFlat()
pramod.driveCar()

