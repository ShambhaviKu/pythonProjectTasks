# *args and **kargs

def Numb(*args):
    for i in args:
        print(i)


def addnum(*args):
    additn = 0
    for i in args:
        additn = additn + i
    print(additn)



# call function
Numb(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

addnum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
