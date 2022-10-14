"""
Swap case (from HackerRank):
https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

Given a string, return a new string where the letters switch case.

Examples:
"Help" -> "hELP"
"let'S Go" -> "LET's gO"
"123 MaiN St." -> "123 mAIn sT."
"""

def swap_case(input_str):
    new_str = "" # Empty string that will eventually hold the converted string
    for letter in input_str:
        if letter.isupper(): # If this is upper-case, change it to lower case
            letter = letter.lower()
        elif letter.islower(): # If lower case, change it to upper case
            letter = letter.upper()
        # print(letter)
        new_str += letter # Concatenate the current letter - put it at the end
        
    return new_str

# print(swap_case("Help"))
# print(swap_case("let'S Go"))
# print(swap_case(""))

# # One-line version
# new_str = "Help".swapcase()
# print(new_str)


"""
First and last index (from Edabit):
https://edabit.com/challenge/AYpxyzbnbS7BGSgvd

Given a string and a character, return a list containing the first and last index of the given character.  If the
character does not appear at all in the string, return "None".

Examples:
"green", "e" would return [2, 3]
"evening moon", "n" would return [3, 11]
"blue", "b" would return [0, 0] as "b" appears only once
"green", "a" would return None
"""

def first_and_last_index(input_str, input_char):
    found_indexes = []
    # Loop through each character in the given string
    for i in range(len(input_str)):
        cur_char = input_str[i]
        print(f"Current character is {cur_char} at index {i}")
        if cur_char == input_char: # Characters match
            # If we have found the character more than 2 times already
            if len(found_indexes) == 2:
                print("Another match found")
                found_indexes[1] = i
                print(found_indexes)
            else: # Found the character for the first or second time
                print("First or second match found")
                found_indexes.append(i)
                print(found_indexes)
    # Check to see whether the given character was found once or not at all
    if len(found_indexes) == 0:
        print("Not found at all")
        return None
    elif len(found_indexes) == 1: # Only found once
        print("Only one occurrence")
        found_indexes.append(found_indexes[0]) # Duplicate the value - first instance is also last instance
        print(found_indexes)
    # We only reach this return statement if we have found the character at least once
    return found_indexes
    

print(first_and_last_index("green","e"))
print(first_and_last_index("evening moon", "n"))
print(first_and_last_index("blue", "b"))
print(first_and_last_index("radar", "i"))
print(first_and_last_index("","e"))
print(first_and_last_index("purple",""))
print(first_and_last_index("",""))

# Tip: Write your ideas in pseudocode.  Even if you can't write the exact code, at least you have
# the general idea right.