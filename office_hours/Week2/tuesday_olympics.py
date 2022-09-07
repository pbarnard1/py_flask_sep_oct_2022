# The code below produces a NameError message!
# myList = [1,2,3,4]
# for i in range(0, len(my_list)):
#     print(i)
#     print(my_list[i])

my_list = [3, 8, 1, 2]
# This version does not use indexes - it grabs each value from the list directly and individually
for i in my_list:
    print(i)

# Compared to
# is an index from 0, 1, 2, up to the last valid index in the list
for j in range(len(my_list)):
    print(j) # Prints the index only - but no value linked to the index
    print(my_list[j]) # Prints the value at the current index j

my_str = "hello world"
for k in my_str:
    print(k)

my_dictionary = {
    "name": "Adrian",
    "city": "Seattle"
}

# The variable p holds each key from the dictionary
for p in my_dictionary:
    print(p) # Prints the name of the current key ONLY
    print(my_dictionary[p]) # Prints the value in the dictionary at the current key
    print(f"Key is {p}: value is {my_dictionary[p]}")

# ERROR
# print(my_list[len(my_list)])

# print(city) # INCORRECT - error because it's looking for a VARIABLE called "city"
print(my_dictionary["city"]) # CORRECT - grabs the value linked to the KEY called "city" in the dictionary "my_dictionary"