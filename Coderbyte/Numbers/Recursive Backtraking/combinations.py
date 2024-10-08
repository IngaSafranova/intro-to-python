# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.


          #### 2 - solutions - #####
def combine(n,k):
  result = []
  solution = []
  
  # start with first number
  def backtrack(num):
    if len(solution) == k:
      result.append(solution[:])
      return
      
    for num in range(num,n +1):
      if num not in solution:
        solution.append(num)
        # backtrack to next number to avoid dublicates
        backtrack(num+1)
        solution.pop()  
      
    pass
  # start with number 1 untill the n  
  backtrack(1)
  
  return result

print(combine(4,2))

class Solution:
    def combine(self, n, k):
        ans, sol = [], []

        def backtrack(x):
            if len(sol) == k:
                ans.append(sol[:])
                return
# we can see how many numbers we have left to choose from (left)
# and how many we still need to chooce
            left = x
            still_need = k - len(sol)
            
 # if we have more numbers left to choose from we can choose not to pick a number
            if left > still_need:
                backtrack(x - 1)
                
 # if we choose to pick a number
 
            sol.append(x)
            backtrack(x - 1)
            sol.pop()

        backtrack(n)
        return ans
