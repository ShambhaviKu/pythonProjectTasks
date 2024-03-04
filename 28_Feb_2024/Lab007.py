class Animal:

    def sound(self):
        print("sound of Animal")

class Dog(Animal):

    def sound(self):
        print("Sound of Dog")

harry = Dog()
harry.sound()