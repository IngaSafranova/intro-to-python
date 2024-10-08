# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root == None:
          return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
    
    # formula to find the height of a tree    
        return 1 + max(left,right)
    print(maxDepth([3,9,20,null,null,15,7]))