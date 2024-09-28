# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

def longestOnes(nums, k):
  
  left = 0
  longest = 0
  number_of_zeros = 0
  
  for right in range(len(nums)):
    # if we have 0
    if nums[right] == 0:
      number_of_zeros += 1
   
   # if we have too many 0 
    while number_of_zeros > k:
      # if left is 0 and will be moved over
      if nums[left] == 0:
        # we have less 0 again
        number_of_zeros -=1
      left += 1
      
    w = right - left + 1
    longest = max(longest,w)
    
  return longest 
    
    
          
         
  # set condition while s[r]=0 and not more than 2 times
  
  # when we have more than 2 0 , move left by 2
  
  
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))