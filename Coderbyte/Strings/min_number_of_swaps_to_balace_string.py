# You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

# A string is called balanced if and only if:

# It is the empty string, or
# It can be written as AB, where both A and B are balanced strings, or
# It can be written as [C], where C is a balanced string.
# You may swap the brackets at any two indices any number of times.

# Return the minimum number of swaps to make s balanced.

# Input: s = "][]["
# Output: 1
# Explanation: You can make the string balanced by swapping index 0 with index 3.
# The resulting string is "[[]]".

def minSwaps(s):
        # count for '['
        count = 0
        # loop the string and count '['
        for char in s:
        # if char is ']' we decrease count as we use up '['
            if char == '[':
                count += 1
            elif char == ']' and count > 0:
                count -= 1    
      # at the end of the loop we have a count of not matched brackets
        # formula to balace them (count + 1)//2  +1 to get ceiling number not floor number after divide         
        #print(count) 
        return (count + 1) //2               
       
print(minSwaps("][]["))       