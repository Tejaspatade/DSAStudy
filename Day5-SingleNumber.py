# Single Number LeetCode 136
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [2,2,1]
Output: 1
"""

class Solution:
    def singleNumber(self, nums) -> int:
        # edge case for length of array is 1
        if len(nums) == 1:
            return nums[0]
        # output variable
        output = 0
        # Iterate all num in nums Time Complexity: O(n)
        for num in nums:
            # XOR the num with current result in output
            output ^= num
        # Space Complexity: O(1)
        return output
# This works because of the way XOR works, XOR between any num and 0=num & XOR between any num and itself is 0. Thus all the duplicates cancel out each other in the output variable no matter the order in which they were XORed. The remaining value is always the unique value in the end