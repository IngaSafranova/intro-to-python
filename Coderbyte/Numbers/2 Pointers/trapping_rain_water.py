# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

def trapped(height):
  # find max height of left and right
  # have 2 pointers
  # to find trapped water we need to substract from max height current height
  # add all results
  left = 0
  right = len(height) -1
  max_left = height[left]
  max_right = height[right]
  result = 0
  while left < right:
    if max_left < max_right:
      left += 1
      max_left = max(max_left, height[left])
      trapped = max_left - height[left]
      result += trapped
    else:
      right -= 1
      max_right = max(max_right, height[right]) 
      trapped = max_right - height[right] 
      result += trapped
  return result  
      

print(trapped([0,1,0,2,1,0,1,3,2,1,2,1]))