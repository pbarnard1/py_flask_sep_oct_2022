"""
Scrabble Score
(From https://edabit.com/challenge/cH5ce3f4QgnreDW4v)
You are given a list of dictionaries, where each dictionary looks like the following:
{"tile": "A", "score": 1}
Your objective is to return the total score from the list of tiles (dictionaries).

Example:
x = [
    {"tile": "P", "score": 3},
    {"tile": "H", "score": 4},
    {"tile": "A", "score": 1},
    {"tile": "N", "score": 1},
    {"tile": "T", "score": 1},
    {"tile": "O", "score": 1},
    {"tile": "M", "score": 3},
]
PHANTOM will return 14 (3 + 4 + 1 + 1 + 1 + 1 + 3).
"""
# INPUT: tile_list is a parameter holding a list of dictionaries, where each dictionary is a tile with a score
def scrabble_score(tile_list):
    sum = 0 # sum represents the total score when we add all the tiles' scores together
    # For loop will go through each tile individually
    for i in range(len(tile_list)): # By default, you start at 0
        # print(tile_list[i]) # Dictionary at index i in the list
        # print(tile_list[i]["score"]) # Grab the score in the dictionary at index i in the list
        sum += tile_list[i]["score"] # Adds the score of the current tile (dictionary) to the sum
    # OUTPUT: the sum of the scores
    return sum

x = [
    {"tile": "P", "score": 3}, # Entry at index 0: x[0]
    {"tile": "H", "score": 4}, # Entry at index 1: x[1]
    {"tile": "A", "score": 1},
    {"tile": "N", "score": 1},
    {"tile": "T", "score": 1},
    {"tile": "O", "score": 1},
    {"tile": "M", "score": 3},
]

# print(x[0]) # Grab dictionary at index 0
# print(x[0]["score"]) # Score in the dictionary at index 0

y = [
    {"tile": "Q", "score": 10},
    {"tile": "U", "score": 1},
    {"tile": "A", "score": 1},
    {"tile": "R", "score": 1},
    {"tile": "T", "score": 1},
]

print(scrabble_score(y))

def scrabble_score_2(tile_list):
    sum = 0
    for current_tile in tile_list:
        # print(current_tile) # Grab tile directly
        sum += current_tile["score"]
    return sum

print(scrabble_score_2(y))
"""
Filter Strings from List
(Modified from this version from Edabit: https://edabit.com/challenge/nunJurLEibCyn8fzn)
Given a list containing strings and numbers, return a new list with all string values removed.
Keep the original order of the values the same.

Examples: 
[3, 8, "hello", -4] should return [3, 8, -4]
["money", "33", 4, "blue", 5] should return [4, 5] ("33" is a string, not a number)
"""

def filter_string(my_list):
    new_list = [] # This initially empty list will hold numeric values only (NO strings)
    for val in my_list: # val is taking each value directly from the list
        # https://www.geeksforgeeks.org/python-type-function/
        if type(val) is not str: # if type(val) != str and "if type(val) is not str" are both equivalent
            new_list.append(val)
    return new_list

z = ["money", "33", 4, "blue", 5]
print(filter_string([3, 8, "hello", -4]))
print(filter_string(z))

def filter_string_v2(my_list):
    new_list = [] # This initially empty list will hold numeric values only (NO strings)
    for val in my_list: # val is taking each value directly from the list
        # https://www.geeksforgeeks.org/python-type-function/
        if type(val) in [int, float]: # Grab ONLY if the value is an integer or a floating (decimal) number
            new_list.append(val)
    return new_list

print(filter_string_v2([3, 8.5, "hello", -4]))
print(filter_string_v2(z))