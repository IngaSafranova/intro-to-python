# You are given a 0-indexed binary string s having an even length.

# A string is beautiful if it's possible to partition it into one or more substrings such that:

# Each substring has an even length.
# Each substring contains only 1's or only 0's.
# You can change any character in s to 0 or 1.

# Return the minimum number of changes required to make the string s beautiful.

def minChanges(s):
  # as tring len is even we can check numbers in pairs. If they both the same, no change needed
  # if not we need to count number of changes
  n = len(s)
  count = 0
  # to check pairs we move i in step 2, so i jumps one iteration
  # i = 0, then i = 2 and sp on
  for i in range(0,n,2):
    if s[i] != s[i+1]:
      count += 1
  return count    
  
print(minChanges( "1001"))