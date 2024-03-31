with open("TestFIle.txt", "r") as file:
    content = file.readlines()
    print(content)

    for i in content:
        print(i, end="")

with open("TestFIle.txt", "a") as file:
    file.write("\nshambhavi")
    file.write("\nyash")
