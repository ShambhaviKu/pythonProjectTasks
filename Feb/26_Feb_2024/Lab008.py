class password:

    def __init__(self, inpassword):
        self.__inpassword = inpassword

    def set_inpassword(self, inpassword):
        if len(inpassword) > 10:
            self.__inpassword = inpassword
            print("validation success")
        else:
            print("weak password")

    def inpassword_auth(self,flag):
        if flag:
            print(self.__inpassword)
            print("successful Authentication")
        else:
            print("Invalid password")

user1 = password("Abc%25698745")

user1.set_inpassword("Abc%25698745")
user1.inpassword_auth(True)



