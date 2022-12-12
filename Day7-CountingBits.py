# Counting Bits 338 Leetcode Easy
"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""

class Solution:
    def countBits(self, n: int):
        # Dynamic Programming Approach dp array
        dp = [0] * (n + 1) 
        # Offset value 1, 2, 4, 8, 16, 32
        offset = 1

        # Iterate all nums from 1 to n
        for num in range(1, n+1):
            # Check if current iteration has reached new offset
            if offset * 2 == num: 
                # Update offset to current num
                offset = num
            # Add the no. of 1s at index of current - offset & 1 to get no. of 1s at current index
            dp[num] = 1 + dp[num-offset]
        return dp