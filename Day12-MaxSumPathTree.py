# Maximum Product of Splitted Binary Tree LeetCode 1339
"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        # Output
        output = [root.val]

        def dfs(root):
            # Base Case for recursion
            if root is None:
                return 0
            # Get max sums of left & right subtree path, omit them only if they are negative values
            maxLeft = max(dfs(root.left), 0)
            maxRight = max(dfs(root.right), 0)

            # check if splitting the path here itself gives better result or else keep it unchanged
            output[0] = max(output[0], root.val + maxLeft + maxRight)

            # Return sum of current + max from its left & right subtree sums
            return root.val + max(maxLeft, maxRight)
        dfs(root)

        return output[0]