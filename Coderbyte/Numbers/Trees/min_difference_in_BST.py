# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Input: root = [4,2,6,1,3]
# Output: 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        min_dif = [float('inf')]
    # var to keep previous node value
        previous = [None]
# helper fc to find difference
        def diff(root):
            if not root:
                return 

    # first we go left            
            diff(root.left)
    # if we have previous node value
            if previous[0] is not None:
            # calc min diference. As it is binary tree we know that previous val is less than current    
                min_dif[0] = min(min_dif[0], root.val - previous[0])  

            previous[0] = root.val
# check right
            diff(root.right)
    # call the function        
        diff(root)
        return min_dif[0]       