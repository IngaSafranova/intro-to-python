# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def sortedArrayToBST(nums):
   
   # helper function
   def Binary(nums, start,end):
     if start > end:
       return None
     
     middle = start + ((start - end)//2) 
     
     node = TreeNode(nums[middle])
     node.left = Binary(nums, start, middle -1)
     node.right = Binary(nums,middle + 1, end)
     
     return node
   
   n = len(nums)
   if n == 0:
     return None
   
   return Binary(nums, 0, n-1)   
    