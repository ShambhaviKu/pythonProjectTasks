
class car:
    name = None
    color = None
    model = None
    speed = None
    engine = None


    def drive(self):
        print("drive")

    def start_engine(self):
        print('started')

    def who_is_driving(self):
        return self.name + " is Driving " + self.model

obj1 = car()
obj1.model = "Tesla"
obj1.name = "shambhavi"
print(obj1.who_is_driving())

obj2 = car()
obj2.model = "lamborgini"
obj2.name = "yash"
print(obj2.who_is_driving())
