# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Example 1:


# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque       
def largestValues( root):

        if root is None:
            return []
          
        q = deque()
        q.append(root)
        result = []
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                #print(node)
                level.append(node.val)
                max_val = max(level)
                #print(max_val)
                

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(max_val)
        return result
        