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