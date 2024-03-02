class kasturvedalogin:
    email = None
    password = None

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def loginsuccess(self):
        if self.password == "password123":
            print("valid password")
        else:
            print("password do not matches")

obj1 = kasturvedalogin("abc@gmail.com", "password123")
obj1.loginsuccess()
print(obj1.email)
print(obj1.password)

print("-----------------")

obj2 = kasturvedalogin("testuser@gmail.com", "password12")
obj2.loginsuccess()
print(obj2.email)
print(obj2.password)

