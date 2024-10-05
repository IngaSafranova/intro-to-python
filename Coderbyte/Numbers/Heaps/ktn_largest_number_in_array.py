# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

import heapq


def findKthLargest( nums, k):
  # make into max heap
  n= len(nums)
  for i in range(n):
    nums[i] *= -1
    
  heapq.heapify(nums)
 
  # in a loop remove k-1 times biggest number
  for _ in range(k-1):
    heapq.heappop(nums)
   # return removed last k times number  
  return -heapq.heappop(nums)  
    
 


print(findKthLargest([3,2,1,5,6,4],2))