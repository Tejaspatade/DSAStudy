# Middle Of the Linked List Leetcode 876
"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head):
        # Length of linked list
        length = 0
        # Temporary pointer to traverse list SC:O(1)
        pointer = head
        # Iterate to End of Singly Linked List TC:O(n)
        while pointer:
            length += 1
            pointer = pointer.next
        
        # Compute Middle Node Index
        middleNode = length // 2;
        pointer = head
        # Iterate Once again To middle node
        for _ in range(middleNode):
            pointer = pointer.next
        
        return pointer