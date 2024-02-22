class car:
    color = None
    Model = None

    def car_detail(self):
        print("car detail: ", self.color, self.Model)

car_color = input("enter car color\n")
car_model = input("enter car model\n")




obj = car()

obj.color = car_color
obj.Model = car_model

obj.car_detail()
