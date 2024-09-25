# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

def search(nums,target):
 # find at which index in the array is smalest number
 left = 0
 right = len(nums)-1
 
 while left < right:
   middle = left + ((right - left)//2)
   if nums[middle] > nums[-1]:
     left = middle +1
   else:
     right = middle
     
 index = left 
 print(index)   
# divide array into 2 arrays - biger_nums and smaller_nums
 big = nums[0:4]
 small = nums[4:]
 print(small)
# check if target in one of them
 for num in big:
   if num == target:
     return nums[num]
 for num in small:
   if num == target:
     return nums[num]
 return -1
    
  
print(search([4,5,6,7,0,1,2,3],8))




