class Animal:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def live(self):
        print("live")
    def eat(self):
        print("eating")
    def __str__(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, weight, height):
        super().__init__(name,age,weight,height)

    def bark(self):
        print("barking")

    def chasing(self):
        print("chasing")
class Cat(Animal):
    def __init__(self, name, age, weight, height):
        super().__init__(name,age,weight,height)
    def meowing(self):
        print("meowing")

class Horse(Animal):
    def __init__(self, name, age, weight, height):
        super().__init__(name,age,weight,height)
    def run(self):
        print("run")
    def riding(self):
        print("it is being rode")

horse = Horse("Horse", 20, 250, 150)
horse.run()
horse.riding()

dog = Dog("Dog", 5, 40, 60)
dog.eat()
dog.bark()
