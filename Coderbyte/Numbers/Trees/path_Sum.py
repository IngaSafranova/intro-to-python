# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
     # helper fc to count current sum while visiting nodes   
        def sum(root,current_sum):
            if not root:
                return False

            current_sum += root.val
# if it is the leaf node, check for target sum
            if not root.left and not root.right:
                return current_sum == targetSum
# check left side or right side
            return sum(root.left,current_sum) or sum(root.right, current_sum)


        return sum(root, 0)




        
        
            