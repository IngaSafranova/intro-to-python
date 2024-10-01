# Given a binary tree, determine if it is height-balanced

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        balanced = [True]
# have helper fc to find the height of tree
        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
    # if we found a problem on left return False and dont go to the right        
            if balanced[0] is False:
                return 0


            right_height = height(root.right)

        # if left - right > 1 return False    
            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0

        # formula to find the height of tree        
            return 1 + max(left_height, right_height)

        height(root)
        return balanced[0]