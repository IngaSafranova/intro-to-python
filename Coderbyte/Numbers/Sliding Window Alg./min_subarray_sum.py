# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2

def minSubArrayLen(target, nums):

  sum = 0
  min_lenght = float('inf')
  left = 0
  
  for right in range(len(nums)):
    sum += nums[right]
     
   # condition for shortening window - sum >= target 
    while sum >= target:
       w = right - left + 1
       min_lenght = min(min_lenght, w)
       sum -= nums[left]
       left += 1
      
     
  
  
  return min_lenght if min_lenght < float('inf') else 0    
  


print(minSubArrayLen(7,[2,3,1,2,4,3]))