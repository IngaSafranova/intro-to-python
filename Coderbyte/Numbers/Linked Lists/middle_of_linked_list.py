# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# SOLUTION 1

class Solution(object):
    def middleNode(self, head):
      # traverse the list and count the lenght
        index = head
        lenght = 0

        while index:
            lenght += 1
            index = index.next
            
      # find middle of it  
        middle_index = lenght//2  
        #print(middle_index)
        
      # go to middle node and point head to next node
      # 5//2 = 2 - so middle node 3  
      # 6//2 = 3 so miidle to return 4 as they ask for second
        for _ in range(middle_index):
            head = head.next
        return head
      
  # SOLUTION 2

class Solution(object):
    def middleNode(self, head):
    # have 2 pointers pointing at the head  
        slow = head
        fast = head
# fast goest twice the pace
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
  # when fast goes out of bound slow pointer will be in the middle of the list          
        return slow          