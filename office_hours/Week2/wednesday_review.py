
# Define classes of gardens and plants

class Garden:
    def __init__(self, soil, length, width):
        self.soil = soil
        self.length = length
        self.width = width
        self.weed_count = 0 # Number of weeds in the garden
        self.plants = [] # List of Plants
        # Hold all the plants in this garden

    # After each day, 1 new weed will grow
    def add_one_day(self):
        self.weed_count += 1
        return self

    def remove_weed(self):
        self.weed_count -= 1
        return self

    def remove_all_weeds(self):
        self.weed_count = 0
        return self

    def add_new_plant(self, new_plant): # new_plant is holding a Plant object
        self.plants.append(new_plant)

class Plant:
    def __init__(self, name, type, color, height):
        self.name = name
        self.type = type
        self.color = color
        self.height = height
        self.is_watered = False

    def water(self):
        self.is_watered = True

    def __repr__(self): # Make output a little more human-readable
        return f"Plant named {self.name}"

# Make a garden
my_garden = Garden("loamy", 10, 8)

# Remove weeds from this garden
my_garden.remove_weed().remove_weed()

plant_1 = Plant("apple", "fruit tree", "red", 8)
plant_2 = Plant("tomato", "food plant", "red", 5)

my_garden.add_new_plant(plant_1)

# print(my_garden.plants)

plant_2.water()

# Accessing all the Plants, then one Plant, then an attribute in a single Plant
print(my_garden.plants)
print(my_garden.plants[0])
print(my_garden.plants[0].name)

# Watering a Plant in a specific Garden
my_garden.plants[0].water()