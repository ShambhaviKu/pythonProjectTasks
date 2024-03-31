import os

path = "/Users/alate/PycharmProjects/pythonProjectTasks/1_March_2024/TestFIle.txt"

with open(path, "a") as file:
    file.write("Writing through path")

with open(path) as file:
    content = file.read()
    print(content)

print(os.getcwd())    #current working directory