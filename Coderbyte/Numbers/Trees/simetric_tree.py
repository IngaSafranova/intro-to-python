# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
    # divide into 2 roots and check if oposite sides are the same    
        def same(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False   

            return same(root1.left,root2.right) and same(root1.right,root2.left)


        return same(root,root)        