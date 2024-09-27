# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

from math import inf


def findMaxAverage(nums, k):
  max_avg = - inf
  current_sum = 0
# make window - subaray of length k
  for i in range(k):
    # count the sum of numbers in it
    current_sum += nums[i]
 # find max_avg for initial subaray put k as float as otherwise wrong calc
  max_avg = current_sum/float(k)
 
 # have loop again to move forward. We start at index k, as we stoped 1 before in first loop 
  for i in range(k,len(nums)):
    # add number on right
    current_sum += nums[i]
    # remove number on left
    current_sum -= nums[i-k]
    
    # find avg of it
    avg =current_sum/float(k)
    # compare with max
    max_avg = max(max_avg,avg)
    print(max_avg)
  return max_avg  
    
      
    
   
# find its avg
# move window to the right by one
# remove from subaray by one from left  
  pass

print(findMaxAverage([1,12,-5,-6,50,3],4))