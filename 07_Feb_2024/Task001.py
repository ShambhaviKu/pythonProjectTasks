''' Write a Python program to calculate the area of a circle given
its radius using the formula area=π×r^2 ( Take pie as 3.14) '''
from math import sqrt

r = float(input('Enter the radios of circle: '))
pi = 3.14
area = pi * r**2
print(area)

'''Create a program that takes two numbers as input and prints whether
 the first number is greater than, less than, or equal to the second number.'''

number1 = 20
number2 = 22

condition1 = number1 > number2
print(condition1)

condition2 = number1 < number2
print(condition2)

condition3 = number1 == number2
print(condition3)

#Develop a Python script that calculates the square and cube of a given number.

Number = input("Enter Number: ")
Square = 10**2
Cube = 10**3
print(Square)
print(Cube)

Num = int(input("Enter a number: "))
print(sqrt(Num))
