# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

#  1 -> 2 -> 4
#  1 -> 3 -> 4

# 1 -> 1 -> 2 -> 3 -> 4 -> 4
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # have dummy node to start new node
        dummy = ListNode()
        # put current pointer on dummy head
        current = dummy
        current.next = None
        dummy.next = None
        # while we have 2 lists check wich first value is less
        while list1 and list2:
            if list1.val < list2.val:
             # current.next grabs smaller head   
                current.next = list1
               # that is our current head 
                current = list1
                 # head from this list move to next position
                list1 = list1.next
            else:
                current.next= list2
                current = list2
                list2 = list2.next   

   # if values are the same or one of the lists finishes
        current.next = list1 if list1 else list2
     # return dummy node next as head of new node   
        return dummy.next          
        
     