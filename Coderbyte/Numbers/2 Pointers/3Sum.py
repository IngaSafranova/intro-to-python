# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) =0

def threeSum(nums):
  # have 3 pointers, i for first index, left for second,right for last

  left = 1
  right = len(nums)-1
  answer = []
  # sort the list
  nums.sort()
  print(nums)
  # check i not > 0
  for i in range(len(nums)):
    if nums[i] > 0:
      break
   # check that it is not the same number,skip if yes 
    elif i > 0 and nums[i] == nums[i -1]:
      continue
  # check if 3 numbers adds to 0
  while left < right:
      sum = nums[i] + nums[left] + nums[right]
    
      if sum == 0:
  # if yes store indeses in answer list
         answer.append([nums[i],nums[left],nums[right]])
         print(answer)
         left += 1
         right -= 1
    # check that numbers not as previous     
         while left < right and nums[left] == nums[left -1]:
           left += 1
         while left < right and nums[right] == nums[right+1]:
           right -= 1  
  # if too small move left
      elif sum < 0:
        left += 1
    # if too hight move right    
      else:
        right -= 1
        print(f'r - {right}')
  
  
    
  return answer
print(threeSum([-1,0,1,2,-1,-4]))