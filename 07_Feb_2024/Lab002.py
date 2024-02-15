#Strings are immutable


txt = "shambhavi"

x = txt.replace("s", "S")  # replaced string returns a new string with the replaced content

print(x)
print(txt)

print(txt[0])
print(txt[-1])

#String Slicing
print(txt[0:9])
print(txt[0:9:2])

name2 = 'I love orange'
print(name2[0:20:5])  #Ien
print(len(txt))

# Reverse Slicing
a = 'Hie everyone'
print(a[10:5:-1])
print(a[ :4])
print(a[: : -1])

str = a[0:2] + a[3: ]

del str
print(str)

name = None
print(type(name))


char = "itswrite\tkkkkkkkkk"
print(char)

a= -10
print(-a)
ch = True
print(not ch)

a = 5  # binary: 101
print(~a)  # Prints: -6, binary: -110

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)
a = 5
b = 5
print(a is b)

print('---------')

a=10 #1010
b=11 #1011
print(a&b) # 1010

a = 9
print(~a)







