# Find All Numbers Disappeared in an Array LeetCode 448
"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Input: nums = [1,1]
Output: [2]
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        # Mark existing values from nums at their indices with negative nos
        # Time Complexity: O(n)
        # Iterate all num from nums
        for num in nums:
            # The index where num should be is num-1 in a sorted array
            # Note: Using abs() since the value there might already be negatively marked
            index = abs(num) - 1
            # Set number at index to negative indicating it exists somewhere else in nums array
            nums[index] = -1 * abs(nums[index])
            
        # Traverse Array and append missing values to output array
        output = []
        for index, num in enumerate(nums):
            # If num is positive, this indicates that it's index + 1 isn't in nums array
            if num > 0:
                # Adding to output array
                output.append(index + 1)
        return output
        