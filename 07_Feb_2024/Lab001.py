#set operator
set = {1,2,3,4,5,'hi',6,1}
set2 = {1,2,3,4}
print(set)

#list operator
list = [1,2,3,4,5,6,6,4]
list[0] = 10
list.reverse()
print(list)

a = []
a.insert(0,1)
a.insert(1,10)
a.insert(2,23)
a.insert(2,78)
a.insert(3,12)
a.append(985)
a.remove(1)
a.reverse()
a.extend([20,21,23])
a.pop(1)
a.pop()
print(a[2:5])
print(a)


#Bitwise operator
b = 8^7
print(b)