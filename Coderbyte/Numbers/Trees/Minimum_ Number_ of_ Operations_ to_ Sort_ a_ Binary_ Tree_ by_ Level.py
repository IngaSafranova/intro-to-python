# You are given the root of a binary tree with unique values.

# In one operation, you can choose any two nodes at the same level and swap their values.

# Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

# The level of a node is the number of edges along the path between it and the root node.

#  Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
# Output: 3
# Explanation:
# - Swap 4 and 3. The 2nd level becomes [3,4].
# - Swap 7 and 5. The 3rd level becomes [5,6,8,7].
# - Swap 8 and 7. The 3rd level becomes [5,6,7,8].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.

 #Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

def minimumOperations( root):
        if root is None:
            return 0
        # helper function nums are name for each level array
        def count_swaps(level):
            swaps = 0
            # make copy of nums which is sorted to know where each number have to be
            sorted_nums = sorted(level)
            # map original array number -> index to know where number is in not sorted level
            # dictionary comprehension
            index_map = {n:i for i,n in enumerate(level)}
            #print(index_map)

            for i in range(len(level)):
                if level[i] != sorted_nums[i]:
                    swaps += 1

                    j = index_map[sorted_nums[i]]
                    #print(j)
                    level[i], level[j] = level[j], level[i]

                    # update index_map after swap so numbers are in correct index
                    index_map[level[i]] = i
                    index_map[level[j]] = j



            return swaps
        queue = deque()
        queue.append(root)
        result = 0
        

        while queue:
            level = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
           
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #print(level)
            result += count_swaps(level)
        return result
        