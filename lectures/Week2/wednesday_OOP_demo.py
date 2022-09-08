class City: # Define a class called City
    organization = "Municipality League" # CLASS VARIABLE
    all_cities = [] # Class variable holding ALL instances of the City class (all Cities)

    def __init__(self, name, population, mayor): # The __init__ method is called when creating an object
        self.name = name # Assigning attributes
        self.population = population
        self.mayor = mayor
        self.landmarks = [] # Initially empty list of Landmarks
        City.all_cities.append(self) # Adding the new City to the class variable all_cities

    # Demo of instance methods
    def add_family(self, family_size): # Notice the "self" at the beginning!
        self.population += family_size # self.attribute_name to grab accordingly!

    def move_out(self, family_size):
        self.population -= family_size

    @classmethod
    def rename_organization(cls, new_name):
        cls.organization = new_name

    @staticmethod
    def is_big_enough(current_population):
        if current_population >= 1000:
            print("Can be incorporated into a city")
            return True
        else:
            print("Not big enough to be incorporated")
            return False

class Landmark:
    def __init__(self, name, year_created, address):
        self.name = name
        self.year_created = year_created
        self.address = address
        self.city = None # Default that will hold the City we're linking to

# Creating instances of the City class
seattle = City("Seattle",741000,"Adrian")
nashville = City("Nashville",694000,"Jenny")

# print(seattle.population) # Grabbing the population of Seattle: variable_name.attribute_name

space_needle = Landmark("Space Needle", 1962, "333 Main St.")

# Demo with an instance method
seattle.add_family(5)
# print(seattle.population)

# Access a class variable
print(City.organization)
print(seattle.organization)

# One way to change a class variable - directly
City.organization = "New City League"
print(City.organization)
print(seattle.organization)

# Print the cities' names individually
print(City.all_cities[0].name)
print(City.all_cities[1].name)

# Another way to change a class variable - with a class method
City.rename_organization("League of Cities")
print(City.organization)

# Static method demo
City.is_big_enough(500)
City.is_big_enough(1500)

# Linking the Space Needle to Seattle
seattle.landmarks.append(space_needle)

# Link Seattle to the Space Needle
space_needle.city = seattle

# Starting with the Space Needle, print the city it's in
print(space_needle.city.name)
# Print the name of a landmark from the city
print(seattle.landmarks[0].name)