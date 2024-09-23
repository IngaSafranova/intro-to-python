# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Input: head = [1,1,2]
# Output: [1,2]
# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def deleteDuplicates(self, head):
      # current is head  
        cur = head
      # while we have current and next nodes
        while cur and cur.next:
          # if current node value is the same as next
            if cur.val == cur.next.val:
              # current node next link links with next nodes next link (skip the node with the same value)
                cur.next = cur.next.next
            else:
              # if value is defferent current node goes to next node
                cur = cur.next
              
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)     