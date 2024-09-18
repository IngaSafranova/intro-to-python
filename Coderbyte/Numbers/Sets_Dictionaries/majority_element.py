# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Input: nums = [3,2,3]
# Output: 3

from collections import defaultdict


def majorityElement( nums):
  nums_dict = defaultdict(int)
  max_key = None
  max_value = 0
  
  
  for num in nums:
    nums_dict[num] += 1
    print(nums_dict)
    
  for key, value in nums_dict.items():
    if value > max_value:
      max_value = value
      max_key = key
  print(max_key)    

print(majorityElement([3,3,4]))