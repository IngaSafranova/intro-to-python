# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Input: nums = [2,2,1]
# Output: 1

from collections import defaultdict

def singleNumber(nums):
  # have a dictionary
  numbers = defaultdict(int)
  
  for num in nums:
    numbers[num] += 1
  print(numbers)  
  # return number from dict with value 1
  for num, val in numbers.items():
    if val == 1:
      return num
  

print(singleNumber( [4,1,2,1,2]))