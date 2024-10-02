# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 
class Solution(object):
    def isValidBST(self, root):
# helper fc takes min and max val
        def binary(root, min_val,max_val):

            if not root:
                return True
 # if node val is <= than min or >= than max
            if root.val <= min_val or root.val >= max_val:
                return False
# on left our max val is current node.val/ on right node.val is min_value
            return binary(root.left, min_val,root.val) and binary(root.right,root.val,max_val)

        return binary(root, float('-inf'), float('inf'))            

