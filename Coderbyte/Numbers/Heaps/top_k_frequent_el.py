# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        # make dict to count occurancies
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        print(nums_dict)           
        # make  min heap
        heap = []
        
        for num,freq in nums_dict.items():
            # push to the heap until lenght is < k
            if len(heap) < k:
                heapq.heappush(heap,(freq,num))
            else:
            # push and pop at the same time so lenght is k    
                heapq.heappushpop(heap,(freq,num))
       # print(heap) 
        # return num value from the heap        
        return (h[1] for h in heap)
  
# Oher way - quicker

# Buckets
from collections import Counter


def topKFrequent(nums, k):
      n = len(nums)
      counter = Counter(nums)
      # keep numbers as values and frequency of numbers as index
      buckets = [[] for i in range(len(counter)+1)]
      
      for num, freq in counter.items():
          buckets[freq].append(num)
        
      ans = []
      # iterate frequency bucket from right ( from most frequent position)
      for i in range(len(buckets)-1,0,-1):
          # it could be more than 1 number stored so we need to loop again at each index
          for num in buckets[i]:
              ans.append(num)
              # when len is k we stop appending
              if len(ans) == k:
                  return ans

# Time Complexity: O(n)
# Space Complexity: O(n)
    
          
       