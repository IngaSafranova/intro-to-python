# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# Input: nums = [1,3,5,6], target = 2
# Output: 1

def searchInsert(nums,target):
  n= len(nums)
  left = 0
  right = n-1
  
  while left <= right:
    middle = left + ((right-left)//2)
    if nums[middle] == target:
      return middle
    elif nums[middle] < target:
      left = middle + 1
    else:
      right = middle -1
  
  # if no target in the array but middle is less than target    
  if nums[middle] < target:
    # target would be in position +1
    return middle + 1
  else:
    return middle      


print(searchInsert( [1,3,5,6],7))