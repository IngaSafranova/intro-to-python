# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

def sortedSquares(nums):
  result = []
  # get first and last numbers
  left = 0
  right =len(nums)-1
  print(left)
  print(right)
  
  # check which is greater and append to result
  while left <= right:
    if abs(nums[left]) > abs(nums[right]):
      result.append(nums[left] **2)
      
    # left pointer move to right  
      left +=1
    else:
      result.append(nums[right]**2) 
    # right pointer move to the left   
      right -= 1
      
  print(result) 
  
  result.reverse() 
  
  return result  
  

print(sortedSquares([-4,-1,0,3,10]))