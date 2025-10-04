class Myclass:
    def __init__(self):
     self._protected_Variable = "This is my protected variable"

    def _protected_method(self):
        print("This is a protected method")

myclass = Myclass()


print(myclass._protected_Variable)
myclass._protected_method()