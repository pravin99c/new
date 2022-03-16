
# # A Python program to demonstrate that hidden
# # members can be accessed outside a class
# class MyClass:
 
#     # Hidden member of MyClass
#     __hiddenVariable = 10
 
# # Driver code
# myObject = MyClass()    
# print(myObject._MyClass__hiddenVariable)

# Python program to demonstrate
# use of class method and static method.
# from datetime import date
  
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
      
#     # a class method to create a Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
      
#     # a static method to check if a Person is adult or not.
#     @staticmethod
#     def isAdult(age):
#         return age > 18
  
# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', 1996)
  
# print (person1.age)
# print (person2.age)
  
# # print the result
# print (Person.isAdult(22))

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))