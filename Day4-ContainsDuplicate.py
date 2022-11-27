# Contains Duplicate Leetcode 217
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
Input: nums = [1,2,3,4]
Output: false
"""

class Solution:
    def containsDuplicate(self, nums) -> bool:
        # Use Hashmap thus space complexity is O(n)
        myHashMap = {}
        # Iterate Array once in worst case thus time complexity is O(n)
        for i in range(len(nums)):
        # Check if value at current iteration index is a duplicate
            if nums[i] in myHashMap:
                # True if it is a duplicate
                return True
            # Add Value to hashmap since its unique
            myHashMap[nums[i]] = 1;
        # If we iterate entire array and dont get a single duplicate, this means the array has no duplicates and we enter false
        return False