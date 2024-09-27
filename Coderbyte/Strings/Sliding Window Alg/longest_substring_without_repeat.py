# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring( s):
 
  # have a set to check for unique char
  sett = set()
  # have count of longest lenght
  longest = 0
  # have 2 pointers
  l = 0
  for r in range(len(s)):
    # if we have char on right in the set already
    while s[r] in sett:
    # remove char from left to try and fix the problem  
      sett.remove(s[l])
    # move left to next index  
      l += 1
  # have current lenght of window  
    w = (r-l) + 1
    longest = max(longest,w)
  # add char on right to the window so we can check is it unique  
    sett.add(s[r])
    
  return longest 
        
      
    
    

print(lengthOfLongestSubstring("abcabcbb"))