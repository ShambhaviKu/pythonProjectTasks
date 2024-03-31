# parameterised function/ return type function

def addTwoNum(a, b):
    return a + b


def GreetMe(name):
    print(f"Hello {name}")


def minimum(a, b):
    if a < b:
        return a
    return b


# call function
Addtn = addTwoNum(2, 5)
print(Addtn)

GreetMe("Shambhavi")

print(minimum(10, 2))
print(minimum(10, 20))
