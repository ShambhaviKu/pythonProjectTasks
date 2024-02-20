my_dict = {'b': 2, 'a': 1, 'c': 3}

for k, v in my_dict.items():
    if k == "b":
        print("b found")
    else:
        print("Not found")
    print(k, v)

print('b' in my_dict)  #True