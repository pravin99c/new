class Preson:
  
    # class attribute
    attr1 = "hhjak"
  
    # Instance attribute
    def __init__(self, name):
        self.name = name
          
    def speak(self):
        print("My name is {}".format(self.name))
  
# Driver code
# Object instantiation
Rodger = Preson("fcg")
Tommy = Preson("sf")
  
# Accessing class methods
Rodger.speak()
Tommy.speak()
print(Rodger.attr1)