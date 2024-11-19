# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

def maximumSubarraySum(nums, k):
  result = 0
  # map to keep track of previous index of number
  prev_index = {}   # num -> prev index of num
  current_sum = 0
  left = 0
  
  for right in range(len(nums)):
    
    current_sum += nums[right]
    print(f'cur - {current_sum}')
    
    # if num not in map yet we get -1 (out of range index)
    index = prev_index.get(nums[right], -1)
    print(f'index - {index}')
    
    prev_index[nums[right]] = right
    print(prev_index)
    
   # while we have duplicate or window size is too big 
    while left <= index or right - left + 1 > k:
      print(f'left = {left}')
      current_sum -= nums[left]
      left += 1
      
    if right - left + 1 == k:
      result = max(result, current_sum)

  return result
      
    
    
  pass

print(maximumSubarraySum([1,5,4,2,9,9,9],3))