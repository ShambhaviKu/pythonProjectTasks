class operations:

    def area(self,a = None, b = None):
        if a != None and b != None:
            print("area of rectangle", a * b)

        elif a != None:
            print("area of circle", 3.14 * a**2)

        else:
            print("None")

shape = operations()
shape.area()
shape.area(10)
shape.area(10,20)