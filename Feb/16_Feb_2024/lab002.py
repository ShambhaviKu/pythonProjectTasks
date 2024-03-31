# function

def sqrt(i):
    return i**2

sqr = sqrt(2)
print(sqr)

sqr1 = sqrt(4)
print(sqr1)

sqr2 = sqrt(5)
print(sqr2)

numbers = [1, 2, 3, 4, 5]

# Map() -
# 1. Takes Each item from the list
# 2. execute the function on it.
# 3. Return same number of elements ( list)

sq_numbers = list(map(sqrt,numbers))
print(sq_numbers)