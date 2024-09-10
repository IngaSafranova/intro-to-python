# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

def findClosestNumber( nums):
  
  # choose first num in list as closest
  closest_number = nums[0]
  for number in nums:
    # if absolute value of number is less than closest, swap
    if abs(number) < abs(closest_number):
      closest_number = number
  print(closest_number) 
  
  # if closest number is negative and positive value is in the list   
  if closest_number < 0  and abs(closest_number) in nums:
    
   # return positive value
    return abs(closest_number)
  else:
    return closest_number
  
print(findClosestNumber( [-4,-2,1,4,8]))    