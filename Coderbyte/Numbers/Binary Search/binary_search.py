# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4

def search(nums,target):
  n = len(nums)
  left = 0
  right= n-1
  
  
  while left <= right:
    # find middle index of array
    middle = left + ((right- left)//2)
    print(middle)
    # if middle index value is target
    if nums[middle] == target:
      #return index
      return middle
    # if value is too small
    elif nums[middle] < target:
      # move left one over middle to the right
      left = middle+1
    else:
      right = middle -1
  # if escaped the loop - False no target number    
  return -1      

print(search([1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,16,17,18,19,20], 21))