# You are given the root of a binary tree and a positive integer k.

# The level sum in the tree is the sum of the values of the nodes that are on the same level.

# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

# Note that two nodes are on the same level if they have the same distance from the root.
# Input: root = [5,8,9,2,1,3,7,4,6], k = 2
# Output: 13
# Explanation: The level sums are the following:
# - Level 1: 5.
# - Level 2: 8 + 9 = 17.
# - Level 3: 2 + 1 + 3 + 7 = 13.
# - Level 4: 4 + 6 = 10.
# The 2nd largest level sum is 13.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def kthLargestLevelSum(self, root, k):
      queue = deque()
      queue.append(root)
      ans = []
      
      while queue:
        n = len(queue)
        sum_val = 0
        
        for _ in range(n):
          node = queue.popleft()
          sum_val += node.val
          
          if node.left: queue.append(node.left)
          if node.right: queue.append(node.right)
        ans.append(sum_val)
      print(ans)
      size = len(ans)
      if k > size:
        return -1
      ans.sort()
      return ans[-k]
    
    print(kthLargestLevelSum([5,8,9,2,1,3,7,4,6],2))      
        