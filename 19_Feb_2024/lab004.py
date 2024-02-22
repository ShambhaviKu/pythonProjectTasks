class calculator:

    def sum(self,a,b):
        return a + b

    def diff(self,x,y):
        return x - y

    def mult(self,p,q):
        return p * q

    def div(self,m, n):
        return m/n

obj1 = calculator()
print("summation", obj1.sum(10,20))
print("Differance", obj1.diff(30,20))
print("Multiplication", obj1.mult(30,20))
print("Division", obj1.div(30,20))