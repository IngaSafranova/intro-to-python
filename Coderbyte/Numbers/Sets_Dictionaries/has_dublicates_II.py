# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Input: nums = [1,2,3,1], k = 3
# Output: true

def containsNearbyDuplicate(nums, k):
  # have map to keep numbers num:index
  nums_map = {}
  # iterate the array
  for index in range(len(nums)):
     # if num already in the map we have a dublicate
    if nums[index] in nums_map:
    # check the distance between indeses, if <=k return True   
      if (index - nums_map[nums[index]]) <= k:
        return True
     # else put the num into map  
    nums_map[nums[index]] = index  
 
 
 


print(containsNearbyDuplicate([1,2,3,1],3))