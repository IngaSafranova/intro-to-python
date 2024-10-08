# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

import heapq


def lastStoneWeight(stones):
  n= len(stones)
  # make into max heap
  for i in range(n):
    stones[i] = -stones[i]
  print(stones) 
  heapq.heapify(stones)
  print(stones) 
  # take 2 top value from heap
  while len(stones) > 1:
    stone1 = -heapq.heappop(stones)
    stone2 = -heapq.heappop(stones)
    print(stone1, stone2)
  # compare them
    if stone1 > stone2:
     # if one is bigger put difference back into heap 
      new_stone = stone1 - stone2
      heapq.heappush(stones,-new_stone)
  print(stones)
   # return heap
  if stones:
    return -heapq.heappop(stones)
  else:
    return 0

  
 
  pass
print(lastStoneWeight([2,7,4,1,8,1]))