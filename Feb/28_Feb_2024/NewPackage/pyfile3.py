def read_from_db():
    print("Reading from DB")


class UtilsDB:

    def __init__(self):
        self._protected_var = "Protected"
        self.public_var = "public"
        self.__private_var = "private"

    def readDBMySQL(self):
        print("Reading rorm MYsql")


u = UtilsDB()
print(u.public_var)
print(u._protected_var)