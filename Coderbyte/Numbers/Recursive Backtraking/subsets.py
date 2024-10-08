# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

def subsets(nums):
  n = len(nums)
  result = []
  # temp array to keep copies for solution 
  solution = []
  # helper function to travers the list
  def backtrack(i):
    # if we are at the leaf node - last number in array
    if i == n:
      # append copy of solution at that moment to result
      result.append(solution[:])
      # return to node above
      return
  # Don`t pick a nums[i]
    backtrack(i+1) 
  
  # Pick a number in nums[i]
  
  # put number into solution array
    solution.append(nums[i])
  # move to next index
    backtrack(i+1)
  # remove number from solutions array to start fresh
    solution.pop()
  
  # call function at index 0  
  backtrack(0)  
  return result
  
   


print(subsets([1,2,3]))