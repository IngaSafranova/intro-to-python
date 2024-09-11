# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence( s, t):
  s_lenght = len(s)
  t_lenght = len(t)
  a =0
  b=0
  subsequence = []
  
  # if s is empty
  if s == '':
    return True
  # if s longer then t
  if s_lenght > t_lenght:
    return False
  # loop throug both strings letter by letter
  while a < t_lenght and b < s_lenght:
    # check if chars are the same, append to new list
    if t[a] == s[b]:
      subsequence.append(s[b])
      a += 1
      b += 1
       # if not the same go to next char
    else:
      a += 1
  print(subsequence)
  result = ('').join(subsequence)
  print(result) 
  # if new list and s are the same return true
  if s == result:
    return True
  else:
    return False     
    
  
  

print(isSubsequence('abc','ahbgdcbe'))

# Other solution

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)
        if s == '': return True
        if S > T: return False

        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S-1:
                    return True
                j += 1
        
        return False
      # Time: O(T)
      # Space: O(1)