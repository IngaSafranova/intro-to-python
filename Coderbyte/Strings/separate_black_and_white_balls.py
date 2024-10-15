# There are n balls on a table, each ball has a color black or white.

# You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.

# In each step, you can choose two adjacent balls and swap them.

# Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.

# Input: s = "101"
# Output: 1
# Explanation: We can group all the black balls to the right in the following way:
# - Swap s[0] and s[1], s = "011".
# Initially, 1s are not grouped together, requiring at least 1 step to group them to the right.

def minimumSteps(s):
  # count 0
  zero_count = 0
  # have ans = 0
  ans = 0
  # iterate from right to left
  for char in s[:: -1]:
  
    if char == '0':
      zero_count += 1
    
  # when we come across 1 we add 0-count to ans, because that 1 will have to move right accross those 0    
    else:
      ans += zero_count
  return ans    
       
 
  pass
print(minimumSteps('0111'))