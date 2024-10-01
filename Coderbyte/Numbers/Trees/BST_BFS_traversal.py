# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return None
        
        queue = deque()
        queue.append(root)
        ans = []
        
        while queue:
            # to have list in the answer
            level = []
            n = len(queue)
            # to put each level on diff lists
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left: queue.append(node.left)                
                if node.right: queue.append(node.right)
            
            ans.append(level)

        return ans

