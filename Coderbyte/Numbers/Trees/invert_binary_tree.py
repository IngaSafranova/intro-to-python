# Given the root of a binary tree, invert the tree, and return its root.

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

#            4                            4
#      2         7                  7             2
#  1      3    6     9          9      6       3      1

# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def invertTree(self, root):
        if root == None:
          return
        
        root.left,root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
      
    print(invertTree([4,2,7,1,3,6,9]))    
      