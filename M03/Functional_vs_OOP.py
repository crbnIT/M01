# 10.1
# Creating then printing class Thing
class Thing:
    pass
print(Thing)
# creating and printing an object from class thing
example = Thing()
print(example)
# printed values are different. it prints the class vs the location of the instance of the class

# 10.4
# Creating class Element
class Element:
    # setting up initialization function
    def __init__(self, name, symbol, number):
        # setting attributes
        self.name = name
        self.symbol = symbol
        self.number = number
# creating instance of Element
hydrogen = Element("Hydrogen", "H", 1)
# printing the attributes
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)

# 10.5
# creating the dictionary
dict1 = {
    "name": "Hydrogen",
    "symbol": "H",
    "number": 1
}
# creating second instance of Element, this time using dictionary values to set attributes
hydrogen2 = Element(dict1["name"], dict1["symbol"], dict1["number"])
# printing the attributes
print(hydrogen2.name)
print(hydrogen2.symbol)
print(hydrogen2.number)

# 10.9
# Creating a class for bear, bunny and octothorpe
class Bear:
    # creating the eats() method
    def eats(self):
        print("Berries")
class Rabbit:
    # creating the eats() method
    def eats(self):
        print("Clover")
class Octothorpe:
    # creating the eats() method
    def eats(self):
        print("Campers")
# Creating instances of each different class
ted = Bear()
bunny = Rabbit()
hashtag = Octothorpe()
# Calling the eats() method for each instance
ted.eats()
bunny.eats()
hashtag.eats()
