class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old")
    def make_sound(self):
        print("Meow")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a Dog. My name is {self.name}. I am {self.age} years old")
    def make_sound(self):
        print("Bark")

Cat1 = Cat("Jark", 2.5)
Dog1 = Dog("Tyson", 10)
for a in (Cat1, Dog1):
    a.make_sound()
    a.info()