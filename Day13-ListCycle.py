# Linked List Cycle Easy Leetcode 141
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        # Use Floyd's Tortoise & Hare Problem TC:O(n)
        # Both pointers start at head SC:O(1)
        slow, fast = head, head

        # Keep iterating while fast doesn't find tail of list
        # Checking if fast.next is also not None bcuz fast jumps 2 nodes
        while fast and fast.next:
            # Slow jumps 1 node
            slow = slow.next
            # Fast jumps 2 nodes
            fast = fast.next.next
            # When both pointers meet, this implies list has cycle
            if slow == fast:
                return True
        # Loop Terminated means fast found tail of list
        return False