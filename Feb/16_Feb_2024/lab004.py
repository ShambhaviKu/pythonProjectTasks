# Filter
# It can filter the items from the list based on the logic
# return less number of items

number = [1, 2, 3, 4, 5, 6]


def even(i):
    return i % 2 == 0


even_number = list(filter(even, number))
print(even_number)
