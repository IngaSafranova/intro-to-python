# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious 
# subsequence
#  among all its possible subsequences.


# Input: nums = [1,3,2,2,5,2,3,7]

# Output: 5

# Explanation:

# The longest harmonious subsequence is [3,2,2,2,3].

def findLHS( nums):
  map = {}
  max_count = 0
  # have nums in the map to see how many of each num we have
  for num in nums:
    if num not in map:
      map[num] = 1
    else:
      map[num] += 1
  print(map)  
  
  # for each num in map
  for num in map:
    # check do ve have num + 1
    if (num+1) in map:
      # count how many num and num+1 we have all together
      # that will show the lenght of subsequence
      max_count = max(max_count, (map[num] + map[num+1]))
  return max_count       
  

print(findLHS([1,3,2,2,5,2,3,7]))