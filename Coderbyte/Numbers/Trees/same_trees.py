# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):

        def same(p,q):
        # if both missing - they the same    
            if not p and not q:
                return True
        # if 1 missing - not the same        
            if (p and not q) or (q and not p):
                return False
            if p.val != q.val:
                return False
        # check left and right at the same time        
            return same(p.left,q.left) and same(p.right,q.right)

        return same(p,q)          
                          