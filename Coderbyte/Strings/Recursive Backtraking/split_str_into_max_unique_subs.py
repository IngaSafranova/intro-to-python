# Given a string s, return the maximum number of unique substrings that the given string can be split into.

# You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

# A substring is a contiguous sequence of characters within a string.

# Input: s = "ababccc"
# Output: 5
# Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

def maxUniqueSplit(s):
  # set to track unique substrings
  seen_substrings = set()
  
  # helper backtrack fc
  def backtrack(s,i,seen_substrings):
    n = len(s)
    # if strings is empty
    if i == n:
      return 0
    # count for unique substrings
    max_count = 0
    # iterate string from second index
    for end in range(i+1, n+1):
      # extract the substring each time adding one more char at the end 
      substring = s[i:end]
      print(substring)
      if substring not in seen_substrings:
        seen_substrings.add(substring)
        print(seen_substrings)
        max_count = max(max_count, 1 + backtrack(s,end ,seen_substrings))
        print(max_count)
        seen_substrings.remove(substring)
    return max_count
        
  return backtrack( s,0,seen_substrings)

print(maxUniqueSplit("ababccc"))