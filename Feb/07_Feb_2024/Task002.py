#Use the ternary operator to find the maximum of three numbers entered by the user.


a = int(input("enter number1= "))
b = int(input("enter number2= "))
c = int(input("enter number3= "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

#Develop a Python script that calculates the square and cube of a given number.

Number = int(input("Enter No. to calculate square and cube: "))
print("Square of a number: ", Number**2)
print("Cube of a number: ", Number**3)