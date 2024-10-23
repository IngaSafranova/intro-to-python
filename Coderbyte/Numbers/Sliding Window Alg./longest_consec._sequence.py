# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

# You must write an algorithm that runs in O(n) time.


# Input: nums = [2,20,4,10,3,4,5]

# Output: 4

def longestConsecutive(nums):
# make a set with distinct numbers
  nums_set = set(nums)
  print(nums_set)
  
  longest = 0
  
  for num in nums_set:
    # if number is first in a sequence
    if num -1 not in nums_set:
      count = 1
      # count how many numbers a in a sequence
      while num + count in nums_set:
        count += 1 
    longest = max(longest, count)  
  return longest   

print(longestConsecutive([0,3,2,5,4,6,1,1]))