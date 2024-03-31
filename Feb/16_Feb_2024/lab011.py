my_tuple = (1, 2, "koel", "parot", "peckok")
set(my_tuple)

myset = set(my_tuple)
print(myset)
print(type(myset))

set1 = {1, 2, 3, 3}
set2 = {4, 5, 6}
print(set1.union(set2))

set1 = {1, 2, 3, 3}
set2 = {4, 5, 6, 3}
print(set1.intersection(set2))

set1 = {1, 2, 3, 3, 10, 11, 15}
set2 = {4, 5, 6, 1, 2, 3}
print(set1.difference(set2))
print(set2.difference(set1))
