#break

# n = 1 ------ 10
#break when n = 5

i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

print("------------------")

i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
