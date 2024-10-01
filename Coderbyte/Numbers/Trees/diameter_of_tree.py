# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
# global parameter. [0] to show its global and stores the info at address at [0] in comp memory
        max_height = [0]

    # helper fc to find height of each node    
        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)

            diameter = left + right

            max_height[0] = max(max_height[0],diameter)
            
            return 1 + max(left,right)
            
        height(root)
        return max_height[0]
        
       


