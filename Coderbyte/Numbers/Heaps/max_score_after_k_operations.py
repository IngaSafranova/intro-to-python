# You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

# In one operation:

# choose an index i such that 0 <= i < nums.length,
# increase your score by nums[i], and
# replace nums[i] with ceil(nums[i] / 3).
# Return the maximum possible score you can attain after applying exactly k operations.

# The ceiling function ceil(val) is the least integer greater than or equal to val.

# Input: nums = [10,10,10,10,10], k = 5
# Output: 50
# Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.

import heapq
import math
def maxKelements(nums, k):
# have ans array
  ans = 0
  # make negative number list to create max_heap
  for i in range(len(nums)):
    nums[i] = -nums[i]
  
# make max heap
    heapq.heapify(nums)
  print(nums)

# for k times
  for _ in range(k):
# take max value from heap and add to answer
    max_val = -heapq.heappop(nums)
    print(max_val)
    ans += max_val
    # push to heap ceil(nums[i]/3)
    new_number = math.ceil(max_val/3)
    print(f'new- {new_number}')
    heapq.heappush(nums, -new_number)
  return ans  
    
    


print(maxKelements([1,10,3,3,3],3))