# You are given a string s.

# You can perform the following process on s any number of times:

# Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
# Delete the closest character to the left of index i that is equal to s[i].
# Delete the closest character to the right of index i that is equal to s[i].
# Return the minimum length of the final string s that you can achieve.

# Example 1:

# Input: s = "abaacbcbb"

# Output: 5

# Explanation:
# We do the following operations:

# Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
# Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".

from collections import defaultdict
def minimumLength( s):
  if len(s) < 3:
    return len(s)
  # count all letters in a string
  letter_count = defaultdict(int)
  result = 0
  for char in s:
    letter_count[char] += 1
  for char, count in letter_count.items():
    # if count is odd
    if count % 2 == 1:
     # we need to reduce count to 1 char
      letter_count[char] = (count + 1) - count
    else:
      # if even we need to keep 2 char
      letter_count[char] = (count + 2) - count 
  print(letter_count)     
  result = sum(letter_count.values())
  return result
    
  pass
print(minimumLength('abaacbcbb'))