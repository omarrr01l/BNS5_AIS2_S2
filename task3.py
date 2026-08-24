from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    def describe(self):
        print(f"I am an animal named {self.name}.")

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
class Cow(Animal):
    def make_sound(self):
        return "Moo!"

if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    cow = Cow("Bessie")

    animals = [dog, cat, cow]

    for animal in animals:
        animal.describe()
        print(f"Sound: {animal.make_sound()}")
        print("-" * 30)