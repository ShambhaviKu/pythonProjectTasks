class GF:

    def __init__(self, Lpassword):
        self.__Lpassword = Lpassword

    def home1(self):
        print("Pune")

    def setVilla(self, Lpassword):
        if len(Lpassword) == 4:
            self.__Lpassword = Lpassword
        else:
            print("invalid Pin")

    def is_son(self, is_son):
        if is_son:
            print("Access")
            print(self.__Lpassword)
        else:
            print("Access denied")


class Father(GF):

    def home2(self):
        print("Goa")


class son(Father):

    def home3(self):
        print("Kolhapur")


son1 = son(65223)
son1.is_son(False)
son1.home1()
son1.home2()
son1.home3()

father = Father(2365)
father.home1()
father.home2()

grandFather = GF(5632)
grandFather.home1()

