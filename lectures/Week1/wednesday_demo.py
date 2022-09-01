bank = 300
is_boardwalk_available = True

# Checking two conditions that must be true
if bank >= 400 and is_boardwalk_available == True:
    print("You can buy Boardwalk!")
else:
    print("You cannot buy Boardwalk.  Sorry...")

# Only need one to be true
value = 3
if value < 1 or value > 10:
    print("Value must be from 0 to 10")

# Checking a set of conditions separately
grade = 95
if grade >= 90:
    print("Great job!!")
elif grade >= 80:
    print("Good job!")
elif grade >= 70:
    print("You're doing fine!")
else:
    pass # Add your own code here


# Two ways to loop through a list and checking whether each value is even or odd
x = [5, 1, 4, 6, 3]

for i in range(len(x)): # i will be a value = 0, 1, 2, 3, 4 (NOT including 5)
    if x[i] % 2 == 0: # Number is even
        print(f"{x[i]} is even")
    else:
        print(f"{x[i]} is odd")

for val in x: # Another way to loop through values WITHOUT using the index
    if val % 2 == 0: # Number is even
        print(f"{val} is even")
    else:
        print(f"{val} is odd")

# Find the max value in a list and return it.  If the list is empty, return None.
def find_max_value(my_list):
    if len(my_list) == 0: # Edge case where the list is empty
        return None
    max_value = my_list[0] # First value from the list
    for this_value in my_list: # Loop through the list's values, one at a time
        if this_value > max_value: # If the current value is bigger than the maximum found to this point
            max_value = this_value # Make the current value the new maximum value
    return max_value # Watch where the "return" statement is tabbed!!

# Various test cases
some_list = [3, 1, 7, 10, 3, 2, 5]
print(find_max_value(some_list))
print(find_max_value([1, 0, 3]))
print(find_max_value([]))
