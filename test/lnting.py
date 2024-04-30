"""
This module contains functions for counting occurrences in a list.
"""
def count_occurrences(list_, dog):
    count = 0
    for thing in list_:
        if thing == dog:
            count += 1
    return count
