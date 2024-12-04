# You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
# Return the modified string after the spaces have been added.

# Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
# Output: "Leetcode Helps Me Learn"

def addSpaces(s, spaces):
   # allocate approx space for efficiency.
   # have letter as placeholeder, none or 0 did not work in vs code
      result = ['a'] * (len(s) + len(spaces))
      # pointer for space
      space_ind = 0
      # pointer for result index
      string_ind = 0

      for char_ind in range(len(s)):
            if space_ind < len(spaces) and char_ind == spaces[space_ind]:
                result[string_ind] = ' '
                string_ind += 1
                space_ind += 1

            result[string_ind] = s[char_ind]
            string_ind += 1

      return "".join(result[:string_ind])
    
print(addSpaces("spacing",[0,1,2,3,4,5,6]))