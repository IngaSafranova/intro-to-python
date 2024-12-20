# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

# For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.

# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

# The level of a node is the number of edges along the path between it and the root node.

# Example 1:

# Input: root = [2,3,5,8,13,21,34]
# Output: [2,5,3,8,13,21,34]
# Explanation: 
# The tree has only one odd level.
# The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque

def reverseOddLevels(root):
  # have a queue
  queue = deque()
  # put root to queue
  queue.append(root)
  # have level count
  level = 0
  
  while queue:
     # if level is odd swap values of nodes
    if level & 1:
     # have pointers for nodes
      left = 0
      right = len(queue) -1
      while left < right:
        queue[left].val, queue[right].val = queue[right].val, queue[left].val
        left += 1
        right -= 1
    for _ in range(len(queue)): 
      # pop node from queue 
      node = queue.popleft()
      print(node)
       # if node has children put them into queue
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    level += 1
  return root
      
    
  
 
  
 
  print(reverseOddLevels([2,3,5,8,13,21,34]))