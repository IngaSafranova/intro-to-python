# You are given a 0-indexed array of strings words and a 2D array of integers queries.

# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:

# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].

def vowelStrings(words, queries):
  # have vovels in a set
  vowel_set = ('aeiou')
  n = len(words)
  count = 0
  result = [0] * len(queries)
  
  # make list with extra index at begining to check for range start with 0
  prefix_sum = [0]* (n+1)
        # iterate words and see if first and last letters are in vowel set
  for index, word in enumerate(words):
    # if yes it starts and ends with vowel
    if word[0] in vowel_set and word[-1] in vowel_set:
      count += 1
    # have a sum of such words for each index of words list
    # we have index+1 because we have extra space at begining in prefix_sum array. So for first word at index  0 we will strore count at index 1
    prefix_sum[index + 1] = count
  print(prefix_sum)
  
  for index, query  in enumerate(queries):
    l,r = query
    
    result[index] = prefix_sum[r + 1] - prefix_sum[l]
  return result
        
        
        # to find the words in range substrackt from higher index + 1 lower index sum
  pass
print(vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]))