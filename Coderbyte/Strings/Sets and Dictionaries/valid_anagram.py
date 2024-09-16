# Given two strings s and t, return true if t is an  anagram of s, and false otherwise.

# Input: s = "anagram", t = "nagaram"
# Output: true

from collections import defaultdict


def isAnagram( s, t):
  # make both into dict
  # to use default constructor use integer as default value
  s_dict = defaultdict(int)
  t_dict = defaultdict(int)
  
  # if key not in dict - new will be made
  for letter in s:
    s_dict[letter] +=1
    print(s_dict)
    
  for letter in t:
    t_dict[letter] += 1
    print(t_dict)
    
  # check are they the same
  if s_dict == t_dict:
    return True
  else:
    return False
  
 
print(isAnagram("ram","cat")) 