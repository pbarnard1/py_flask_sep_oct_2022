x = [3, 4, 1, 6, 7, 2, 3]

# Grab the value 1 from x
print(x[2])

# Dictionary
my_profile = {
    "name": "Adrian",
    "city": "Seattle",
    "color": "Yellow",
    "is_happy": True,
    "age": 25,
}

print(my_profile["city"])

# Change the city to "Portland"
my_profile["city"] = "Portland"
print(my_profile)
print(my_profile["city"])
my_profile.pop("age") # one way to remove the "age" key
# del my_profile["age"] # Another way to remove "age" key
print(my_profile)


city_nicknames = {
    "Seattle": "Emerald City",
    "Chicago": "Windy City",
    "Reno": "Biggest Little City in the World"
}

for city, nickname in city_nicknames.items(): # Using .items() method
    print(f"The nickname for {city} is {nickname}")

# Lists of dictionaries
tv_shows = [
    {
        "id": 1,
        "title": "Press Your Luck",
        "network": "ABC",
    },
    {
        "id": 2,
        "title": "Star Trek",
        "network": "NBC",
    },
    {
        "id": 3,
        "title": "Modern Family",
        "network": "ABC",
    },
]

# Accessing a specific value
print("-------------------------------")
print(tv_shows)
print(tv_shows[1])
print(tv_shows[1]["title"])

# More lists with dictionaries

x = [
    {"id": 1, "name": "Melissa"},
    {"id": 3, "name": "Adrian"},
    {"id": 6, "name": "John"},
]

# # INCORRECT
# for id, name in x.items(): # x is a list, NOT a dictionary; .items() is for a dictionary
#     print(f"Persion #{id} is {name}")

# Three ways to show each person's ID and name
for person in x: # person is a dictionary; we are looping through a LIST, so each item happens to be a dictionary (person)
    # print(person)
    # print(person["id"])
    print(f"Person #{person['id']} is {person['name']}") # Watch out with quotation marks - don't mix them up!

for i in range(len(x)):
    print(f"Person #{x[i]['id']} is {x[i]['name']}")

for i in range(len(x)):
    this_person = x[i] # Grabs the current dictionary at index i
    print(f"Person #{this_person['id']} is {this_person['name']}")