# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

###### IT IS LIKE FIBONACCI NUMBERS
def climbStairs( n):
  # have base cases
  if n == 1:
    return 1
  if n == 2:
    return 2
  
  dp = [0]*n
  dp[0] = 1
  dp[1] = 2
  
  # we start at next position after base cases till
  for i in range(2, n):
    dp[i] = dp[i-2] + dp[i-1]
    
  return dp[-1]
  pass

print(climbStairs(3))