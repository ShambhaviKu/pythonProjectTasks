try:
    with open("TestFIle.txt", 'a') as file:
        file.write("This is an additional text\n")
        file.write("This is an additional text2\n")
except FileNotFoundError as fn:
    print(fn)

finally:
    print("Writing done")
