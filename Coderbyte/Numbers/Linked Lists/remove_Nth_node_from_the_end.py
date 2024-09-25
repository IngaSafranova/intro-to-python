# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        ahead = behind = dummy

        # put ahead pointer in n+1 position
        for _ in range(n+1):
            ahead = ahead.next
       # print(ahead) //node 3

        # move both pointers at the same speed
        # when ahead goes out of bounds behind will be in position to skip needed node
        while ahead:
            ahead = ahead.next
            behind = behind.next
# attach behind.next to node atfer the skipped one
        behind.next = behind.next.next
        
        return dummy.next     