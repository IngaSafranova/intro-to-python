# You are given two 0-indexed strings str1 and str2.

# In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

# Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

# Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

# Input: str1 = "abc", str2 = "ad"
# Output: true
# Explanation: Select index 2 in str1.
# Increment str1[2] to become 'd'. 
# Hence, str1 becomes "abd" and str2 is now a subsequence. Therefore, true is returned.

def canMakeSubsequence(str1, str2):
        str1_lenght = len(str1)
        str2_lenght = len(str2)
        str2_index = 0

        for str1_index in range(str1_lenght):
            if str2_index < str2_lenght and (str1[str1_index] == str2[str2_index] or
            ord(str1[str1_index]) + 1 == ord(str2[str2_index]) or
            ord(str1[str1_index]) - 25 == ord(str2[str2_index])):
                str2_index += 1

        return str2_index == str2_lenght

print(canMakeSubsequence('abc', 'ad'))