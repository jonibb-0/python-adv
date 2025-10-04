class Myclass:
    def __init__(self):
     self.__private_Variable = "This is my private variable"

    def __private_method(self):
        print("This is a private method")

myclass = Myclass()

#Error
print(myclass.__private_Variable)
myclass.__private_mthod()