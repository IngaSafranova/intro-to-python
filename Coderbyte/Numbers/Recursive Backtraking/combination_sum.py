# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

def combinationSum(candidates, target):
  
  nums = candidates
  result = []
  solution = []
  
  def backtrack(i, curr_sum):
    # if we found target sum
    if curr_sum == target:
      result.append(solution[:])
      return 
    
    # if curr_sum too big or we went to the end of nums
    if curr_sum > target or i == len(nums):
      return
    
    # deside not to pick a number
    backtrack(i+1, curr_sum)
    
    # we pick a number
    solution.append(nums[i])
    backtrack(i, curr_sum + nums[i])
    solution.pop()
  
  backtrack(0,0)
  return result

print(combinationSum([2,3,6,7],7))