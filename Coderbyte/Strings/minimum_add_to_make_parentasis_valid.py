# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# Input: s = "())"
# Output: 1

def minAddToMakeValid(s):
  # counters for both parentasis
  open_brackets = 0
  closing_brackets = 0
  
  for char in s:
    if char == '(':
      open_brackets += 1
    if char == ')':
      # if char is ')' and we have count for '(', reduce the count 
      if open_brackets > 0:
        open_brackets -= 1
       # else increase the count for closing parentasis  
      else:
        closing_brackets += 1    
 
 # return the sum of both, as it represents unmatched parentasis and we need to close all of them
  
  return open_brackets + closing_brackets
  


print(minAddToMakeValid('())'))