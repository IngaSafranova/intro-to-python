# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

# Return the largest number of chunks we can make to sort the array.


# Example 1:

# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
# Example 2:

# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

def maxChunksToSorted( arr):
  current_max = -1
  result = 0
  # as array is from (0 - n-1) to make it sorted number must corespond to index.
  for index, number in enumerate(arr):
    # we traverse the array and keep track of current max which is current number
    current_max = max(number, current_max)
    # if number correspond to index we can make split as it could be sorted
    if current_max == index:
      result += 1
  return result
  pass

print(maxChunksToSorted([0,3,1,2]))