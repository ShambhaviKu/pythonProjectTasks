class Animal:
     def animalinfo(self):
         return "this is animal class"

class Dog(Animal):

    def rocky(self):
        return "I am dog"

class Cat(Animal):

     def kitty(self):
         return "I am cat"

object = Dog()
print(object.animalinfo())
print(object.rocky())

object2 = Cat()
print(object2.animalinfo())
print(object2.kitty())