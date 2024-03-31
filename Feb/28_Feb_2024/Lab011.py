#Abstraction

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):

    def sound(self):
        print("Bhow Bhow")

class Cat(Animal):

    def sound(self):
        print("mew mew")

object1 = Dog("rocky")
object1.sound()

object2 = Cat("billi")
object2.sound()



