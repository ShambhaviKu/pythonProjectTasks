# Tuple - Collection of items

# List - Collection of items
# mutable -

my_list = [1, 2, 3, 4, 5]

my_list[0] = 11
print(my_list)
print(type(my_list))
print(len(my_list))

my_tuple = (1, 2, 3, 4, 8, 7)
print(my_tuple)
print(len(my_tuple))
print(type(my_tuple))

tulist = list(my_tuple)
print(tulist)
print(type(tulist))
tulist.append(10)
print(tulist)
my_tuple = tuple(tulist)
print(my_tuple)