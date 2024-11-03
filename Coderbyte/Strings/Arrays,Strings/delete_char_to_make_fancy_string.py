# A fancy string is a string where no three consecutive characters are equal.

# Given a string s, delete the minimum possible number of characters from s to make it fancy.

# Return the final string after the deletion. It can be shown that the answer will always be unique.

# Input: s = "leeetcode"
# Output: "leetcode"

def makeFancyString( s):
  # have a string for result
  result = []
  # iterate the string and check the last 2 char in the result list
  for char in s:
    # if they are not the same as our current char - append, if the same - skip
    if len(result) < 2 or not (result[-1] == result[-2] == char):
      result.append(char)
  return ('').join(result)    
  
  pass

print(makeFancyString('leeetcode'))