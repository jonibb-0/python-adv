# from abc import ABC, abstractmethod
# class Person(ABC):
#      def __init__(self, name, age,weight, height):
#          self.name = name
#          self.age = age
#          self.weight = weight
#          self.height = height
#
#      @property
#      def wheight(self):
#          return self._weight
#
#      @wheight.setter
#      def weight(self,value):
#          if value <= 0:
#              raise ValueError("Wheight cant be negativ number.")
#          self._weight = value
#
#      @property
#      def height(self):
#          return self._height
#
#      @height.setter
#      def height(self, value):
#          if value <= 0:
#              raise ValueError("Height mus be an positive number")
#          self._height = value
#
#
#      @abstractmethod
#      def calculate_bmi(self):
#          pass
#
#      @abstractmethod
#      def get_bmi_category(self):
#          pass
#
#      def print_info(self):
#          print(f"{self.name}, Age: {self.age}, Weight: {self.weight} kg, Height: {self.height} m,"
#                f"BMI: {self.calculate_bmi():.2f}, Category: {self.get_bmi_gategory()}")
#
#
# class Adult(Person):
#     def calculate_bmi(self):
#         return   self.wight / (self.height **2)
#
#     def get_bmi_category(self):
#         bmi = self.calculate_bmi()
#         if bmi < 18.5:
#             return "Underweight"
#         elif 18.5 <= bmi < 24.9:
#             return "Normal weight"
#         elif 24.9 <= bmi <29.9:
#             return "Overweight"
#         else:
#             return "Obese"
#
#
# class Child(Person):
#     def calculate_bmi(self):
#         return self.wight / (self.height ** 2) * 1.3
#
#     def get_bmi_category(self):
#         bmi = self.calculate_bmi()
#         if bmi < 14:
#             return "Underweight"
#         elif 14 <= bmi < 18:
#             return "Normal weight"
#         elif 18 <= bmi < 24:
#             return "Overweight"
#         else:
#             return "Obese"
#
# class BMIApp:
#     def __init__(self):
#         self.people = []
#
#     def add_person(self, person):
#         self.people.append(person)
#
#
#     def collect_user_data(self):
#
#         name = input("Enter name: ")
#         age = int(input("Enter age: "))
#         weight = float(input("Enter weight: "))
#         height = float(input("Enter height: "))
#
#         if age>= 18:
#             person = Adult(name,age,weight,height)
#         else:
#             person = Child(name,age,weight,height)
#
#
#         self.ad_person(person)
#
#     def print_results(self):
#
#         for person in self.people
#             person.print_info()
#
#     def run(self):
#
#         while True:
#             self.collect_user_data()
#             cont = input("Do you want to add another person? (yes/no").strip().lower()
#             if cont != 'yes':
#                 break
#             self.print_results()
# app.BMIApp()
# app.run()