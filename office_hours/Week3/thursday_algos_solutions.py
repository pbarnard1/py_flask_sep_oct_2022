"""
Frequency distribution (from https://edabit.com/challenge/KKmM4ob5wwPwf8kgS):

Given a list of items, return a dictionary that contains the frequency of each item.
Each key will be an entry from the list, and the value linked to the key will be
the number of occurrences of said key in the list.  If the list is empty, return
an empty dictionary.

Examples:
["M", "P", "C", "C", "P"] returns { "M": 1, "P": 2, "C": 2} as there are 2 "P"s, 2 "C"s and 1 "M"
[1, 5, 8, 5, 5, 3] returns { 1: 1, 5: 3, 8: 1, 3: 1 } (Note it's okay that a key is a number or boolean)
[] returns {}
"""

def freq_distribution(my_list):
    freq_dictionary = {} # Start with an empty dictionary that will fill itself as we go
    # for loop to go through the list
    for item in my_list:
        # One method would be to loop through the dictionary to find whether a key exists
        # for key in freq_dictionary.keys():
        print(f"Current item is {item}")
        is_item_found = False # Assume the current item is NOT in the frequency dictionary
        for key in freq_dictionary:
            print(f"Current key in frequency dictionary is {key}")
            if key == item: # If the key matches the current item
                print(f"Key matches item: {item}")
                is_item_found = True
                freq_dictionary[key] += 1 # Add 1 to the value linked to the key (or item)
                print("New frequency dictionary:")
                print(freq_dictionary)
        if not is_item_found:
            freq_dictionary[item] = 1 # Add new key to frequency dictionary and set its value to 1 to start
            print(f"Adding {item} to frequency dictionary")
            print("New frequency dictionary:")
            print(freq_dictionary)
    return freq_dictionary

example_1 = ["M", "P", "C", "C", "P"]
print(freq_distribution(example_1))

def freq_distribution_2(my_list):
    freq_dictionary = {} # Start with an empty dictionary that will fill itself as we go
    # for loop to go through the list
    for item in my_list:
        # One method would be to loop through the dictionary to find whether a key exists
        if item in freq_dictionary: # If the key is in the dictionary
            print(f"{item} found in frequency dictionary")
            freq_dictionary[item] += 1 # Add one to the value
            print(freq_dictionary)
        else: # Not in frequency dictionary
            print(f"{item} NOT in frequency dictionary - adding now")
            freq_dictionary[item] = 1 # Add item to the dictionary and set its value to 1 to start
            print(freq_dictionary)
    return freq_dictionary

print(freq_distribution_2(example_1))

"""
# Number of digits in a number (https://edabit.com/challenge/yFJzLfYghz7ZtsyAN)

Given an integer as input, return the number of digits in the integer.
You may assume the number is an integer (whole number) only.

Examples:
24 -> 2 digits
23849 -> 5
0 -> 1
-15 -> 2 (don't count the "-")
"""

def count_digits(num):
    if num < 0:
        num = num * -1 # Removes the "-" by multiplying by -1 (-1 * 5 = -5, -1 * -3 = 3); could also do abs(num) for absolute value
    num_str = str(num) # Convert number to a string
    return len(num_str) # Return number of characters in string
    # return len(str(abs(num))) # One-line version

print(count_digits(500))
print(count_digits(23984237))
print(count_digits(0))
print(count_digits(-3))

def count_digits_2(num):
    num_str = str(num) # Convert number to a string
    if num < 0: # If negative
        return len(num_str) - 1 # Subtract one so we don't count the "-" sign
    else: # 0 or positive
        return len(num_str)

# Advanced mathematical version with no string
def count_digits_3(num):
    new_num = abs(num) # Take absolute value
    num_digits = 1
    # Examples: 33 % 10 = 3, 33 % 100 = 33 (100 = 10 ^ 2)
    # 589 % 10 = 9, 589 % 100 = 89, 589 % 1000 = 589 (1000 = 10 ^ 3)
    # Keep raising to a power of 10 until the remainder is the same as the number (in terms of absolute value)
    while new_num != new_num % (10 ** num_digits):
        num_digits += 1
    return num_digits

print(count_digits_3(-222))
print(count_digits_3(22))
print(count_digits_3(222))
print(count_digits_3(1000))