# You are given two string arrays words1 and words2.

# A string b is a subset of string a if every letter in b occurs in a including multiplicity.

# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.

# Return an array of all the universal strings in words1. You may return the answer in any order.

#  Example 1:

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
# Output: ["facebook","google","leetcode"]
from collections import defaultdict
from collections import Counter
def wordSubsets( words1, words2):
        result = []
        # words2  merged dictionary
        map = defaultdict(int)
        for word in words2:
            # count all characters of the word and put into dict
            map_2 = Counter(word)
            # merge the words into one char count for all of the words in words2.
            for char, count in map_2.items():

                map[char] = max(map[char], count)
        print(map)
              
        for word in words1:
            # count char in each word
            map_1 = Counter(word)
            flag = True
            for char, count in map.items():
            
              # compare letter count of both dictionaries
              # if words1 word has leser count of the same letter than word2 
                if map_1[char] < count:
                    flag = False
             
                    break
            # if True - all letters are compared and condition is true        
            if flag:
                result.append(word)

       
            
        return result
print(wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]))