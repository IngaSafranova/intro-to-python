# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix( strs):
  min_length = float('inf')
  i = 0
  # find shortest string
  for string in strs:
    if len(string)< min_length:
      min_length = len(string)
  # loop throug string    
  while i < min_length:
    for string in strs:
      
      # check each strings letter agains first string,
      # if dont match return all before the problematic char
      if string[i] != strs[0][i]:
        return string[:i]
    i += 1
    
  return string[:1]    
   
   


print(longestCommonPrefix( ["flower","flow","flight"]))