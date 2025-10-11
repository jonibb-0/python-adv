from lesson9.animal import animal


class Animal:
    def __init__(self,name):
        print("This generic animal sound")
        self.name = name

    def sound(self,):
        print("This generic sound")

    def  description(self):
        print(f"this animal is named: {self.name}")

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Woof, Woof")

    def description(self):
        super().description()
        print(f"breed: {self.breed}.")



class Cat(Animal):
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Meow, Meow")

    def description(self):
        super().description()
        print(f"Color: {self.color}.")


animal = Animal("Generic Animal" )
animal.sound()
animal.description()

dog = Dog("Maxi", "Pitbull")
dog.sound()
dog.description()

cat = Cat("Clara","Black")
cat.sound()
cat.description()