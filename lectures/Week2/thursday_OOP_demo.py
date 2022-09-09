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

class NewCity: # Define a class called City
    organization = "Municipality League" # CLASS VARIABLE
    all_cities = [] # Class variable holding ALL instances of the City class (all Cities)

    def __init__(self, data): # data is a dictionary
        self.id = data["id"]
        self.name = data["name"] # Assigning attributes
        self.population = data["population"]
        self.mayor = data["mayor"]
        self.landmarks = [] # Initially empty list of Landmarks

class NewLandmark:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.year_created = data["year_created"]
        self.address = data["address"]
        self.city = None # Default that will hold the City we're linking to

# Creating instances of the City class
seattle = City("Seattle",741000,"Adrian")
nashville = City("Nashville",694000,"Jenny")

space_needle = Landmark("Space Needle", 1962, "333 Main St.")

# Linking Seattle and the Space Needle
seattle.landmarks.append(space_needle)
space_needle.city = seattle

print(space_needle.city.population)
print(seattle.landmarks[0].year_created)

# Creating objects with dictionaries

seattle_dictionary = {
    "id": 1,
    "name": "Seattle",
    "population": 741000,
    "mayor": "Adrian"
}

nashville_dictionary = {
    "id": 2,
    "name": "Nashville",
    "population": 694000,
    "mayor": "Jenny"
}

new_seattle = NewCity(seattle_dictionary)
new_nashville = NewCity(nashville_dictionary)

space_needle_dictionary = {
    "id": 1,
    "name": "Space Needle",
    "year_created": 1962,
    "address": "333 Main St."
}

pike_place_market = {
    "id": 2,
    "name": "Pike Place Market",
    "year_created": 1920,
    "address": "120 Pine St."
}

new_space_needle = NewLandmark(space_needle_dictionary)
new_pike_place = NewLandmark(pike_place_market)

city_list = [new_seattle, new_nashville]
print(city_list)
for this_city in city_list:
    print(this_city.name)

# Link landmarks to Seattle
new_seattle.landmarks.append(new_space_needle)
new_seattle.landmarks.append(new_pike_place)

# Loop to show the name of each landmark in Seattle
for this_landmark in new_seattle.landmarks:
    print(this_landmark.name)