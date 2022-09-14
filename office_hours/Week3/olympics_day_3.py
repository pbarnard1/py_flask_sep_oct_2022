x = [3, 4, '5', 6]
for i in x:
    print(i)

# for i in range(len(x)):
#     print(i)

y = [
    {"name": "Adrian", "age": 25},
    {"name": "Kimmy", "age": 33}
]

for j in y:
    print(j) # j is the current value - a dictionary
    print(j["age"]) # Grab value from dictionary

def add_nums(num1, num2):
    print(num1 + num2)

# add_nums(6,5)
# add_nums(3, "4") # ERROR
# add_nums("3", 4) # ERROR
# add_nums("2", "3") # Okay - effectively concatenating (putting together) strings

print(add_nums(6,5)) # Note the None because the function doesn't return anything

def add_nums_2(num1, num2):
    return num1 + num2

this_sum = add_nums_2(3,4)
print(this_sum)


class Pet:
    def __init__(self, name):
        self.pet_name = name
        self.couches_ruined = 0

    # def __repr__(self):
    #     return f"Pet object whose name is {self.pet_name}"
my_pet = Pet("Pete")
# print(couches_ruined) # ERROR
# print(self.couches_ruined) # ERROR
print(my_pet.couches_ruined) # Runs OK