"""
Check subset (from HackerRank):
https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

Given two lists of values, determine whether the first list's values can all be found in the second list.  
In other words, is the first list, A, a subset of the second list, B?
Return True if so, False if not.

Examples:
[2, 5, 7] and [8, 5, 7, 4, 2] returns True as 2, 5 and 7 are all found in the second list
[2, 2, 3] and [8, 2, 3, 5] returns False as while 2 and 3 are found, there is only a single 2 in the second list
[] and [4, 5] returns True.  An empty list is a subset of an empty list technically.
"""

# This does NOT work for duplicate values!
# def check_subset(list_1, list_2):
#     # is_subset = True
#     for val_1 in list_1:
#         is_value_found = False
#         for val_2 in list_2:
#             if val_1 == val_2:
#                 is_value_found = True
#                 break # Exits the inner for loop early
#         if not is_value_found:
#             return False
#     return True

# Suggestion by Matthew: Maybe remove the value from each list and see what's left at the end, particularly the first list?

# Frequency distribution: Make a dictionary for each list and count how many times each value appears, then we can compare
# and see whether each value from the list appears at least as many times in the second list

def check_subset(list_1, list_2):
    if len(list_1) > len(list_2): # Edge case: first list is bigger, so it can't be a subset of the second list
        return False
    elif len(list_1) == 0: # An empty set is a subset of any set (an empty list is a subset of any list)
        return True

    # Part 1: Make a dictionary for each list and count how many times each value appears.  In the dictionary,
    # the key is a number from the original list, and the value is the number of times that that number was found.
    list_1_freq_dictionary = {}
    list_2_freq_dictionary = {}
    # First list
    for val in list_1:
        if val in list_1_freq_dictionary: # If found already found
            list_1_freq_dictionary[val] += 1 # Add one to count (frequency)
        else: # New value, so create a new key and set its initial count (frequency) to 1
            list_1_freq_dictionary[val] = 1
    # Second list
    for val in list_2:
        if val in list_2_freq_dictionary:
            list_2_freq_dictionary[val] += 1
        else:
            list_2_freq_dictionary[val] = 1
    print(list_1_freq_dictionary)
    print(list_2_freq_dictionary)
    
    # Part 2: Compare the keys in both dictionaries
    for key in list_1_freq_dictionary:
        print(f"Current number from list 1: {key}")
        # print(f"Number of times in list 1: {list_1_freq_dictionary[key]}")
        # print(f"Number of times in list 2: {list_2_freq_dictionary[key]}")
        if key not in list_2_freq_dictionary or list_1_freq_dictionary[key] > list_2_freq_dictionary[key]:
            return False
    return True

print(check_subset([2, 5, 7], [8, 5, 7, 4, 2]))
print(check_subset([2, 2, 3], [8, 2, 3, 5]))
print(check_subset([2, 7, 3], [8, 2, 3, 5])) # Edge case: value in 1st list isn't in second list
print(check_subset([2, 7, 3, 4], [2, 3, 5]))
print(check_subset([], [2, 3, 5]))