class City: # Define a class called City
    def __init__(self, name, population, mayor): # The __init__ method is called when creating an object
        self.name = name # Assigning attributes
        self.population = population
        self.mayor = mayor
        self.landmarks = [] # Initially empty list of Landmarks
    
    # Demo of instance methods
    def add_family(self, family_size): # Notice the "self" at the beginning!
        self.population += family_size # self.attribute_name to grab accordingly!

    def move_out(self, family_size):
        self.population -= family_size

class Landmark:
    def __init__(self, name, year_created, address):
        self.name = name
        self.year_created = year_created
        self.address = address
        self.city = None # Default that will hold the City we're linking to

# Creating instances of the City class
seattle = City("Seattle",741000,"Adrian")
nashville = City("Nashville",694000,"Jenny")

print(seattle.population) # Grabbing the population of Seattle: variable_name.attribute_name

space_needle = Landmark("Space Needle", 1962, "333 Main St.")

# Demo with an instance method
seattle.add_family(5)
print(seattle.population)
