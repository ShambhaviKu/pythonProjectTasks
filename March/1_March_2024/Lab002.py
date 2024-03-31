try:
    a = int(input("Enter value: "))
    b = int(input("Enter value: "))
    result = a/b
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print(f"Result: {result}")
finally:
    print("end")



