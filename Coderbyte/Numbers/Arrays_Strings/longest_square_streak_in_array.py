# You are given an integer array nums. A subsequence of nums is called a square streak if:

# The length of the subsequence is at least 2, and
# after sorting the subsequence, each element (except the first element) is the square of the previous number.
# Return the length of the longest square streak in nums, or return -1 if there is no square streak.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [4,3,6,16,8,2]
# Output: 3
# Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
# - 4 = 2 * 2.
# - 16 = 4 * 4.
# Therefore, [4,16,2] is a square streak.
# It can be shown that every subsequence of length 4 is not a square streak.

def longestSquareStreak(nums):
  # make set with unique nums
  # iterate the nums and treat each num as beginning of a streak
  # if num*num exist in set increase count
  # when streak finished update max count
  unique_nums = set(nums)
  max_count = 0
  
  for num in nums:
    current = num
    count = 0
    while current in unique_nums:
      count += 1
      if current * current == 10**5:
        break
      current *= current
    max_count = max(max_count,count) 
  if max_count > 1:
    return max_count
  else:
    return -1 
        
  

print(longestSquareStreak([4,3,6,16,8,2]))