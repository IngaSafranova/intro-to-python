# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# 9
# 8     |
# 7     |                   |
# 6     |   |               |       |
# 5     |   |               |       |
# 4     |   |       |       |       |
# 3     |   |       |   |   |       |
# 2     |   |       |   |   |   |   |
# 1  |  |   |   |   |   |   |   |   |
# 0  |  |   |   |   |   |   |   |   | 

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

def maxArea(height):
  # have 2 points at each end
  left = 0
  n = len(height)
  right = n-1
  # have max are = 0
  maxArea = 0
  
  while left < right:
    smaller_height = min(height[left],height[right])
    #print(smaller_height)
    distance = right - left
  # pick smaller one and multiply by distace between them
  # thats current are
    current_Area = smaller_height * distance
    #print(current_Area)
 
  # compare max are with current and pick higher
    if current_Area > maxArea:
      maxArea = current_Area
     # print(maxArea)
  # if left pointer is smaller then right - move to the right
    if height[left] <= height[right]:
      left += 1
    else:  
  # else move to the left
      right -= 1
      
  return maxArea    
  

print(maxArea([1,8,6,2,5,4,8,3,7]))