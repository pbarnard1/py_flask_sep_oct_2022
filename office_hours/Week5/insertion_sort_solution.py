"""
Insertion sort:
Implement insertion sort.  

Here is a visual: https://visualgo.net/en/sorting - select "INS" for insertion sort.

Time complexity: O(n^2) [1 + 2 + 3 = 6, 1 + 2 + 3 + 4 = 10, 1 + 2 + 3 + 4 + 5 = 15 => sum from 1 to n is given by n*(n+1)/2]
Space complexity: O(1) - don't need any lists in memory; a variable that has only one value is O(1)
"""

def insertion_sort(num_list):
    # Start with the *second* value, then go to the 3rd, then the 4th, etc.
    for i in range(1,len(num_list)):
        # Check to see whether the current value is smaller than the previous value
        # The current value in the list = num_list[i]
        # Previous value = num_list[i-1]
        print(num_list)
        print(f"The current value is {num_list[i]} at index {i}")
        
        cur_index = i # Starting point for where the current value as we move it backwards until it's inserted in the correct place
        while num_list[cur_index] < num_list[cur_index-1] and cur_index > 0: # While the current value is smaller than the previous one in the list
            # We move this current value backwards by swapping - below is one way
            # x = num_list[cur_index]
            # num_list[cur_index] = num_list[cur_index-1]
            # num_list[cur_index-1] = x
            print(f"Moving {num_list[cur_index]} behind {num_list[cur_index-1]}")
            [num_list[cur_index], num_list[cur_index-1]] = [num_list[cur_index-1], num_list[cur_index]] # Short version of swapping
            cur_index -= 1 # Move the current value's index back by one
    # No need to return the list since the list will stay changed after the function is done

# Test cases

x1 = [8, 4, 10, 3, 15, 22, 5, 3]
y1 = [1, 3]
z1 = [4]
w1 = []
v1 = [3, -1, -2, 5, -8, 0, 12, -15]

print(v1)
insertion_sort(v1)
print(v1)