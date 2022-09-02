"""
Find minimum value of list:
Write a function that accepts a list as input and returns the smallest value
found.  If the list is empty, return None.
"""
# RIOT walk
# R - Read - Read the problem carefully - multiple times - to make sure you understand what is required of you.
# I - Inputs - What inputs will your algorithm need, if any?
# O - Output - What will we get back from the algorithm?
# T - Testing - Test your algorithm with many different test cases.

def min_value_in_list(my_list):
    # Check to see if the list is empty first
    if len(my_list) == 0:
        return None
    else: # If not, then we can proceed checking the list
        min_found = my_list[0] # Start off with the first value
        # Loop that will go through each value in the list
        for i in range(len(my_list)):
            # Check to see whether the current value is the smallest found to this point
            if my_list[i] < min_found: # i is the index, my_list[i] is the value in my_list at index i
                min_found = my_list[i] # Set this value as the minimum
        return min_found

print(min_value_in_list([4, 2, 5, 1, 8]))
print(min_value_in_list([]))
test3 = [1, 8, 3, 2, 0, -5, 10, 6]
print(min_value_in_list(test3))

"""
Count vowels:
Write a function that accepts a string and returns the number of vowels found.
For this exercise, "a", "e", "i", "o" and "u" are vowels - we will not count
"y" as a vowel.

BONUS: Make the function count "A", "E", etc.  In other words, have this function
handle all strings, regardless of case sensitivity.
"""
# One version using a tuple
def count_vowels(my_string):
    vowel_count = 0
    vowels = ('a','e','i','o','u')
    for letter in my_string:
        if letter in vowels: # Check to see if the current letter can be found in the tuple
            vowel_count += 1
    return vowel_count
print('--------------------')
print(count_vowels("money"))
print(count_vowels("adrian"))

# Another version
def count_vowels_2(my_string):
    vowel_count = 0
    for letter in my_string:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            vowel_count += 1
    return vowel_count
print('--------------------')
print(count_vowels_2("money"))
print(count_vowels_2("adrian"))
"""
Factorial:
In mathematics, n! (read "n factorial") is equal to 1 * 2 * 3 * ... * n.
For example:

2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
4! = 1 * 2 * 3 * 4 = 24

Write a function that takes an integer, n, as input and returns the product
1 * 2 * ... * n.  By definition, 0! = 1 and 1! = 1.  If the number
is negative, return 1.
"""
# Added after the office hour and lecture
def factorial(n):
    if n <= 1: # If it's 1, 0 or negative
        return 1
    else:
        total_product = 1 # Start at 1 since we have 1 * 2 * 3 * ....
        for i in range(1,n+1): # Note the n+1 so that n is included; we're starting at 1 instead of 0 (the default)
            total_product = total_product * i
        return total_product

print(factorial(5))
print(factorial(3))
print(factorial(-2))
print(factorial(8))