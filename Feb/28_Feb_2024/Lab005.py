#Hybrid Inheritance

class A:
    def Ainfo(self):
        print("A")

class B(A):
    pass

class C(A):

    def CInfo(self):
        print(C)

class D(B,C):
    pass

obj = D()
obj.CInfo()
obj.Ainfo()

