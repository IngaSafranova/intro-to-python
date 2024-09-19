# iven an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

#You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4

from collections import defaultdict


def longestSeq(nums):
  count = 0
  i = 1
  # put nums into sorted set
  sorted_n = sorted(nums)
  #print(sorted_n)
  nums_dict = defaultdict(int)
  
  for num in sorted_n:
    nums_dict[num] +=1
  print(nums_dict)
  # check if first num +1 = second num
    # count if yes


print(longestSeq([100,4,200,1,3,2,1,2]))
