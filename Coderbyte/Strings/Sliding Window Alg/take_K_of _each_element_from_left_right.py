# You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

# Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

# Input: s = "aabaaaacaabc", k = 2
# Output: 8
# Explanation: 
# Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
# Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
# A total of 3 + 5 = 8 minutes is needed.
# It can be proven that 8 is the minimum number of minutes needed.

from collections import defaultdict
from math import inf

def takeCharacters( s, k):
  
  # have a dict with letter count
  letter_count = defaultdict(int)
  
  for char in s:
    letter_count[char] += 1
  
  # if any letter < k return -1
  if letter_count['a'] < k or letter_count['b'] < k or letter_count['c'] < k:
    return -1
  
  left = 0
  n = len(s)
  result = float(inf)
  
  # traverse the string and add letter into window
  for right in range(n):
    # remove that letter from total count
    letter_count[s[right]] -= 1
    # if adding letter to the window makes total count that is outside the window < k
    # we have invalid condition and need to shrink the window
    while letter_count['a'] < k or letter_count['b'] < k or letter_count['c'] < k:
      letter_count[s[left]] += 1
      left += 1
      
      # to find the lenght of removed letters we do (n = total lenght - window size)
      # we need to find min lenght removable
    result = min(result, (n - (right - left +1)))  
  return result
  
  

print(takeCharacters("aabaaaacaabc",2))