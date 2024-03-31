class shape:

    def area(self):
        print("Area of shape")

class rectangle(shape):

    def __init__(self,width, higth):
        self.width = width
        self.higth = higth

    def Recarea(self):
        print (self.higth * self.width)

class circle(shape):

        def __init__(self,radius):
            self.radius = radius

        def Cirarea(self):
            print(3.14 * self.radius**2)

obj =  rectangle(10, 1)
obj.area()
print(obj.width)
print(obj.higth)
obj.Recarea()

obj2 =  circle(10)
obj2.area()
print(obj2.radius)

obj2.Cirarea()
