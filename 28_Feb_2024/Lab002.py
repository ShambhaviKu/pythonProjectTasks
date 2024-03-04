class vehicle:
    def vehicalInfo(self):
        print("this is vehicle class")
class car(vehicle):

    def carInfo(self):
        print('my car info')

class bicycle(vehicle):
    def bicycleInfo(self):
        print("my bicycle info")

Honda = car()
Honda.carInfo()
Honda.vehicalInfo()

LadyBird = bicycle()
LadyBird.bicycleInfo()
LadyBird.vehicalInfo()