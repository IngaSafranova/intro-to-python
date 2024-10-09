# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

class Solution(object):
    def minRemoveToMakeValid(self, s):
        # have stack for open parentasis
        stack = []
        # make list of separate charackters
        string = list(s)
        
        for i,char in enumerate(string):
            if char.isalpha():
                continue
        # if open bracket keep its index in stack
            if char == '(':
                stack.append(i)
        # if closing bracket        
            elif char == ')':
            # if we have open bracket remove it  from stack as we used it    
                if stack:
                    stack.pop()
                else:
        # if no open brackets available replace closing bracket with space            
                    string[i] = ''
        # if we still have opened brackets left we need to replace them to empty space       
        while stack:
            string[stack.pop()] = ''
# make list to string again
        ans = ('').join(string)
        return ans
                             
        