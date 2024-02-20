import math


def cuberoot(i):
    return math.cbrt(i)


print(cuberoot(1000))

my_list = [27, 250, 500]

cuberoots = list(map(cuberoot, my_list))

print(cuberoots)
