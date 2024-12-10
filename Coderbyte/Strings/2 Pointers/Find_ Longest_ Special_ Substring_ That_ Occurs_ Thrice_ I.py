# You are given a string s that consists of lowercase English letters.

# A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

# Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

# A substring is a contiguous non-empty sequence of characters within a string.

# Input: s = "aaaa"
# Output: 2
# Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
# It can be shown that the maximum length achievable is 2.

def maximumLength( s):
  # have a map to keep frequency of substrings
  string_map = {}
  # iterate the string with 2 pointers for start and end of substring
  for start in range(len(s)):
    current_substring = []
    for end in range(start,len(s)):
      # if its first letter of substring or the same as previous
      if not current_substring or current_substring[-1] == s[end]:
        # we append to current substring
        current_substring.append(s[end])
        # make a list into string
        substring = ''.join(current_substring)
        # put into map
        if substring in string_map:
          string_map[substring] += 1
        else:
          string_map[substring] = 1
      else:
        break
  print(string_map)
  
  answer = 0
  # iterate the map
  for string, freq in string_map.items():
    # if freq > 3 and lenght of substring is more than lenght of answer we keep this string lenght as answer
    # we check the lenght is longer than previous answer as we need to return longest special substring
    if freq >= 3 and len(string) > answer:
      answer = len(string)
  if answer == 0:
    return -1
  return answer
    
  pass
print(maximumLength('aaaa'))