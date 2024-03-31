a = int(input("Enter number "))
b = int(input("Enter number "))

try:
    c = a/b
    print(c)
except Exception as e:
    print(e)
    print("Do not enter b as zero value")