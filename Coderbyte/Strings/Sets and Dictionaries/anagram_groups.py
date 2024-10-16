# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

from collections import defaultdict


def groupAnagrams(strs):
  # have dict where we keep letter count as key and actual string as value
  # use defaultdict and list as default value
  results = defaultdict(list)  # letter count : string
  # iterate the stings list
  for string in strs:
  # have a count for each letter
    count = [0] * 26
  
  # iterate each string and count letters
    for char in string:
      # we can find actii number for each letter
      count[ord(char) - ord('a')] += 1
  # append count - as tuple (list cannot be hashmap key as it is mutable)- and string as value for dictionary
    results[tuple(count)].append(string)
  # return dictionary values, as that our sorted into groups strings
  return results.values()
   
 
print(groupAnagrams(["act","pots","tops","cat","stop","hat"])) 
 
 