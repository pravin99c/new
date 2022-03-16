class petClass:
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

# Create an empty List to store your pet objects

myPetObjects = []

# Create a While loop that continues to ask the user for the information for a new pet object
# Within the loop, create new pet objects with the inputted name and animal type.
# Add this new pet to our pet List
# Ask if the user wants to add more.  If not, exit the While loop

while True:
    new_pet = petClass(input("what type of animal"), input("what is its name"))
    myPetObjects.append(new_pet)
    response = input("add another animal?")
    if response == 'no':
        break 

# Create a new For loop that goes through your pet List.
# Print out the animal type and name of the pets within your List
for pet in myPetObjects:
    print(myPetObjects)