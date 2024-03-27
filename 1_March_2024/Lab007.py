try:
    with open("TestFIle.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError as fnfr:
    print(fnfr)

finally:
    print("file close")
