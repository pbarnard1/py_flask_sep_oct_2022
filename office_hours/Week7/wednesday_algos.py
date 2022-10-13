"""
Min-max sum (from HackerRank):
https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

Given a list of 5 positive integers, find and print the minimum and maximum 
sum you get when adding any 4 of the 5 values.

Examples:
[1, 2, 3, 4, 5] should print 10 (1+2+3+4) and 14 (2+3+4+5)
[5, 8, 3, 6, 2] should print 16 and 22
"""
def min_max_sum(my_list):
    cumulative_sum = 0
    cur_min = my_list[0]
    cur_max = my_list[0]
    # for i in range(len(my_list)):
        # cumulative_sum += my_list[i]
    for val in my_list:
        cumulative_sum += val
        if val < cur_min:
            cur_min = val
        elif val > cur_max:
            cur_max = val
    print(my_list)
    print("Minimum sum:")
    print(cumulative_sum - cur_max)
    print("Maximum sum:")
    print(cumulative_sum - cur_min)

min_max_sum([1, 2, 3, 4, 5])
min_max_sum([5, 8, 3, 6, 2])
min_max_sum([3, 5, 2, 7, 3])



# One technique (not shown): sort the list, 
# then remove the first value to get the max value and for the min sum, remove the last value

"""
Swap case (from HackerRank):
https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

Given a string, return a new string where the letters switch case.

Examples:
"Help" -> "hELP"
"let'S Go" -> "LET's gO"
"123 MaiN St." -> "123 mAIn sT."
"""