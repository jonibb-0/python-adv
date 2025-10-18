class dog:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: Whoof, Whoof")


class cat:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: Meow, Meow")


class bird:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: cu,cu")


Dog = dog("buddy")
Cat = cat("clara")
Bird = bird("pagot")

for animal in (dog,cat,bird):
    animal.sound()