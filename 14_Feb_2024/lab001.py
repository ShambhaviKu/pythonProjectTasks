# Function with multiple parameters

def GreetMe(name="Shambhavi", age=29):
    print(f"Hello {name} {age}")


def addTwoNum(a, b):
    return a + b

#function call

GreetMe()

GreetMe("Shambhavi", "28")


GreetMe("Shambhavi", 28)

GreetMe("Shambhavi")

GreetMe(True, 25)

GreetMe("Shambhavi Kulkarni")

result = addTwoNum(10,20)
result1 = addTwoNum(20,-8)
result2 = addTwoNum("shambhavi ","kulkarni")
#result3 = addTwoNum("abc",20)   can only concatenate str (not "int") to str

print(result)
print(result1)
print(result2)
#print(result3)



