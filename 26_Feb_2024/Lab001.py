class person:
    name = "ravi"
    last_name = None

    last_name = input("enter last name\n")

    def walk(self):
        a = 10
        print(a)
        print(f"{self.name} {self.last_name} can walk")

    def talk(self):
        print(f"{self.name} {self.last_name} can talk")

obj1 = person()
obj1.walk()
obj1.talk()

obj2 = person()
obj2.walk()
obj2.talk()
