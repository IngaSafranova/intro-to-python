# Given two strings s1 and s2, return true if s2 contains a 
# permutation
#  of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

from collections import defaultdict


def checkInclusion(s1, s2):
  n1 = len(s1)
  n2 = len(s2)
  
  if n1 > n2:
    return False
  # have s1 in a dict
  dict_1 = defaultdict(int)
 
  for char in s1:
      dict_1[char] += 1
  
 # make a window in s2 and check if char from set are in it.
  dict_2 = defaultdict(int)
  left = 0
 # make dict 2 same lenght as s1 at first
  for right in range(len(s1)):
    dict_2[s2[right]] += 1 
       
    # print(f' g - {dict_2}')
    # print(dict_1)
    
  if dict_1 == dict_2:
      return True
    
  for right in range(n1,n2):  
      dict_2[s2[right]] += 1    
      dict_2[s2[left]] -= 1
  
      if dict_2[s2[left]] == 0:
        del dict_2[s2[left]]   
      left += 1 
      #print(dict_2)
      if dict_1 == dict_2:
        return True
  
  return False          
      
    
  # if not move window
  
  # if yes return true
  

print(checkInclusion('ab', "eidbaoo"))