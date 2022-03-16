# class Car:
#     car_type = "Sedan"                 #class attribute
#     def __init__(self, name, color):
#         self.name = name               #instance attribute   
#         self.color = color    
# s1=Car('hhh','red')
# print(s1.name)
# print(s1.color)


class Car:   
    car_type = "Sedan" 

    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                 
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

    def max_speed(self, speed):
        return f"The {self.name} runs at the maximum speed of {speed}km/hr"
obj2 = Car("Honda City",24.1)
print(obj2.description())
print(obj2.max_speed(150))