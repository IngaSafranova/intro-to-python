# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# none ->1 -> 2 -> 3 -> 4 -> 5 -> none
# prev curr temp            prev  curr  temp

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # we have dummy pointer - previous
        previous = None
        # pointer for current - starts at head
        current = head
        
        # we iterate the list
        while current:
            # we have one more pointer that starts at next node to head
            temp = current.next
            # move current.next link backwards to link with previous
            current.next = previous
            # move previuous and current up by one position
            previous = current
            current = temp
    # at the end previous will end at last list position - tail
        return previous    