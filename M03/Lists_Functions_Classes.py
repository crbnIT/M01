# Corbyn Eaker
# Lists_Functions_Classes.py
# This program takes user information and creates a car with it, then displays the car's information in an easy to read format

# create the parent class Vehicle with type attribute, moved some attributes off of automobile and into vehicle to be inherited
class Vehicle:
    def __init__(self, type, year, make, model):
        self.type = type
        self.year = year
        self.make = make
        self.model = model

# create the child Automobile class which inherits from the Vehicle class
class Automobile(Vehicle):
    # give it all attributes I'll be asking for, added super() function so it inherits from parent
    def __init__(self, type, year, make, model, door, roof):
        super().__init__(type, year, make, model)
        self.door = door
        self.roof = roof
    # fuction to call in order to print the automobile's information
    def get_info(self):
        print("Vehicle Type: " + user_car.type)
        print("Year: " + user_car.year)
        print("Make: " + user_car.make)
        print("Model:" + user_car.model)
        print("Number of doors: " + user_car.door)
        print("Type of roof: " + user_car.roof)

# collecting user input, storing them in variables
user_type = input("What type of vehicle is this? ")
user_year = input("What is the year? ")
user_make = input("Make? ")
user_model = input("Model? ")
user_door = input("How many doors? ")
roof_type = input("Sun roof?(y/n) ")

# if statement to sort out the sun roof options
if roof_type.lower() == "y":
    user_roof = "Sun roof"
elif roof_type.lower() == "n":
    user_roof = "Solid"
else:
    user_roof = "Unknown"

# user_type is now a parameter just like all other attributes, not sure what i was doing there
# creating the user's automobile, passing the collected inputs into the class parameters
user_car = Automobile(user_type, user_year, user_make, user_model, user_door, user_roof)

# calling function to print automobile's information
user_car.get_info()