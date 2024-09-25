# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        # have dummy node
        dummy = ListNode(self)
        # have 2 pointers - slow and fast pointing at dummy
        slow = fast = dummy
        # connect to head
        dummy.next = head
        # while we have fast pointer and fast.next
        while fast and fast.next:
          # fast pointer will move over 2 nodes while slow over 1
            fast = fast.next.next
            slow = slow.next
       # if slow and fast will ever meet - there is a cycle
            if slow is fast:
                return True
        return False        