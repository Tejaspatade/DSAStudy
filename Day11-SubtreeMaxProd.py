# Maximum Product of Splitted Binary Tree Leetcode 1339
"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root):
        # Array Stores Sum of Every Subtree in a bfs traversal order. Last index stores sum of entire tree. SC:O(n)
        self.subTreeSums = []
        # DFS Traversal, Base Case returns 0 from leaf nodes. TC:O(n)
        def dfs(root):
            # Base Case For Leaf Nodes
            if root is None:
                return 0
            # Left Subtree Call
            leftSum = dfs(root.left)
            # Right Subtree Call
            rightSum = dfs(root.right)
            # Append Sum of current subtree
            self.subTreeSums.append(leftSum + root.val + rightSum)
            # Return Sum of current subtree as well
            return leftSum + root.val + rightSum
        # DFS called from root node
        dfs(root)
        # print(self.subTreeSums)
        # Sum of Entire Tree
        treeSum = self.subTreeSums[len(self.subTreeSums) - 1]
        # Output
        maxProduct = 0
        # Traverse for 
        for i in range(len(self.subTreeSums) - 1):
            # Cutting of at one edge and multiplying the sum for resulting subtrees.
            maxProduct = max(maxProduct, self.subTreeSums[i] * (treeSum - self.subTreeSums[i]))
        # Required modulo answer
        return maxProduct % (10 ** 9 + 7)










