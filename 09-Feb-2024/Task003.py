"""Task -   Factorial series

Factorial

n = 5

5! -->5*4*3*2*1 -> 120

3! -> 3*2*1 -> 6

4! -> 4*3*2*1 -> 24 """

# num = int(input("Enter Number:" ))

number = int(input("Enter a positive number to find its factorial : "))

factorial = 1
while number > 1:
    factorial *= number
    number -= 1

print("factorial of given number is ", factorial)
