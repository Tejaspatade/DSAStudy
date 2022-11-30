# Unique Number of Occurrences LeetCode 1207
"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
"""
# My Solution
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        # Using hashMap SC:O(n)
        occcurences = {}
        # Iterating Array TC:O(n)
        for num in arr:
            # Incrementing num's Occurence
            occcurences[num] = occcurences.get(num, 0) + 1

        # Set for occurence values
        occurenceSet = set(occcurences.values())
        
        # Checking their lengths
        return len(occcurences) == len(occurenceSet)

# Most Optimal Solution
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        # LHS contains unique nums of arr
        # RHS contains set of each num's occurence
        return len(set(arr)) == len(set(Counter(arr).values()))