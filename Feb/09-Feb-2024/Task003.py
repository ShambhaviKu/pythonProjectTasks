"""Task -   Factorial series

Factorial

n = 5

5! -->5*4*3*2*1 -> 120

3! -> 3*2*1 -> 6

4! -> 4*3*2*1 -> 24 """

number = int(input("enter number- "))

if number < 0:
    print("fact")
elif number == 0:
    print("fact - ", 1)
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i  # 1*1*2*3*4*5
    print("factorial of", number, "is", fact)
