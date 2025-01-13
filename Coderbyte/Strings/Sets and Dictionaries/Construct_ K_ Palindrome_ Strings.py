# Given a string s and an integer k, return true if you can use all the characters in s to construct k 
# palindrome strings
#  or false otherwise.
 
# Example 1:

# Input: s = "annabelle", k = 2
# Output: true
# Explanation: You can construct two palindromes using all characters in s.
# Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
from collections import defaultdict
def canConstruct(s, k):
  if k > len(s):
    return False
  odd = 0
  # count all char
  letters = defaultdict(int)
  for char in s:
    letters[char] += 1
  # count how many odd char we have
  # if more then k we need to return false
  for count in letters.values():
    if count % 2 ==1:
      odd += 1
    
  if odd <= k:
    return True
  else:
    return False
    
print(canConstruct("annabelle", k = 2))
