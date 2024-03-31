from abc import ABC, abstractmethod

class ATB(ABC):

    @abstractmethod
    def task1(self):
        pass

    def tast2(self):
        pass

class me(ATB):
    def task1(self):
        print("my 1st task")

    def tast2(self):
        print("my 2nd task")

obj = me()
obj.task1()
obj.tast2()