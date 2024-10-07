# You are given a string s consisting only of uppercase English letters.

# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

# Return the minimum possible length of the resulting string that you can obtain.

# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

#  Input: s = "ABFCACDB"
# Output: 2


def minLength( s):
       stack = []
       for char in s:
            if char == 'B' and stack and stack[-1] == 'A':
                stack.pop() 
            elif char ==  'D' and stack  and stack[-1] =='C':
                stack.pop()
            else:
                stack.append(char)
       return len(stack) 
print(minLength("ABFCACDB"))                 
