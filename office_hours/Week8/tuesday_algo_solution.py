"""
Breaking best and worst records (from HackerRank):
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

See link for full explanation, but the general idea is you're given a list of scores, and you have 
to return the number of times you've broken your record (ties don't count) for highest and lowest scores as a
new list in the form [num_times_high_record_broken, num_times_low_record_broken].  
(The first score doesn't count for breaking a record.)  Assume the list has at least one score in it.

Examples:
[12, 24, 10, 24] would return [1, 1]
[5, 8, 7, 3, 2, 10, 15] would return [3, 2] 
for breaking the maximum score record 3 times (8, then 10, then 15 after the initial score of 5) and
for breaking the minimum score record twice (3, then 2 after the initial score of 5)
"""
def min_and_max_records(score_list):
    # The minimum and maximum scores start off with the first value in the list
    min_score = score_list[0]
    max_score = score_list[0]
    # Start off with 0 times for the number of occasions that the minimum or maximum score record was broken
    min_found_count = 0
    max_found_count = 0
    # Loop through each game's scores
    for score in score_list: # Alternately, do "for i in range(len(score_list)):""
        if score > max_score: # New maximum found
            max_score = score # Make this the new high score
            max_found_count += 1 # The number of times we got a new high score goes up by 1
        elif score < min_score: # New minimum found
            min_score = score
            min_found_count += 1
    return [max_found_count, min_found_count]

print(min_and_max_records([12, 24, 10, 24]))
print(min_and_max_records([5, 8, 7, 3, 2, 10, 15]))