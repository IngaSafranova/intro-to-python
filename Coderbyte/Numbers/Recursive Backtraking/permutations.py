# Given an array nums of distinct integers, return all the possible 
# permutations
# . You can return the answer in any order.

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def permutations(nums):
  n = len(nums)
  result = []
  solution = []
  
  def backtrack():
    # if we hit the leaf node append copy of solution to result
    if len(solution) == n:
      result.append(solution[:])
    
    # loop through numbers  
    for num in nums:
      # use only number not used before
      if num not in solution:
        # apend to solution
        solution.append(num)
        # back to previous node
        backtrack()
        # after backing remove number from solution list to start fresh
        solution.pop()  
    
  
  backtrack()
  return result
  
  
print(permutations([1,2,3]))