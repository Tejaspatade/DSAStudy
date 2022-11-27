# Missing Number Leetcode 268
'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
'''

class Solution:
    def missingNumber(self, nums) -> int:
        # Variable for O(1) Space Complexity
        summation = len(nums)
        
        # O(n) Time Complexity
        for i in range(len(nums)):
            # Addding every value from 0 to length of array - 1 
            summation += i
            #  Subtracting number from nums at current index as well
            summation -= nums[i]
        
        # The final output in summation is the number missing from the array. This is because we added every no. from 0 to length of nums in summation and subtracted out all distinct values of our nums array. Thus, they cancel out each other except for the one value which is going to be missing from our array.
        return summation