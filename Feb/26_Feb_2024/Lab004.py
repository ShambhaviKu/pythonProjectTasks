class vwoliogin:

    def __init__(self):
        self.email = "orrythehero@gmail.com"          #public
        self.__password = "Ast@9856"                  #private
        self._password = "Nhju&456"                   #protected

    def printpass(self):
        print("allowed to use private variables " + self.__password)
        print("allowed to use protected variables " + self._password)

orry = vwoliogin()
print(orry.email)
print(orry.printpass())