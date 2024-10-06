# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

 #Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

def mergeKLists( lists):
  heap = []
 # put lists into min heap in (node.val,index,node) tuple
  for i, node in enumerate(lists):
    # if node list not empty
    if node:
      heapq.heappush(heap,(node.val,i,node))
  # have dummy list for new list
  D = ListNode()  
  current = D  
 # while we have any node in a heap
  while heap:
 # take node from heap and put into new list
    value,i,node = heapq.heappop(heap)
    # attach to node
    current.next = node
    # node becomes current head
    current = node
    # move node to next
    node = node.next
 # after putting node to new list push next node from the same index into the heap
  # if next node is not None
    if node:
      heapq.heappush(heap,(node.val,i,node))
 # return dummy list next
  return D.next
 