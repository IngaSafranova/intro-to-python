# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Input: s = "()"

# Output: true

def isValid(s):
 brackets_map = {
   ')':'(',
   '}':'{',
   ']':'['
 }
 stk = []
 for char in s:
   # if its opening bracket
   if char not in brackets_map:
     stk.append(char)
   else:
     # if its closing bracket, but stk is without any opening brackets
     if not stk:
       return False 
   
   # if its closing bracket, remove last opening braket  
   if char in  brackets_map:
     popped = stk.pop()
     # if no match
     if popped != brackets_map[char]:
       return False 
   # if stack empty and all brakets matched  
   if not stk:
     return True
       



print(isValid("()[]{}") )