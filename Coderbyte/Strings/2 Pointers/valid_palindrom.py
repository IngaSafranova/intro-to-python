# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# NOT EFFICIENT SOLUTION
class Solution(object):
    def isValidPalindrome(self, s):
        # make lowercase
        lower = s.lower()
        # make a list
        s_list = lower.split(' ')
       # print(s_list)
        # remove non alphanumerical char
        new_s = []
        for word in s_list:
            for char in word:
                if char.isalnum():
                    new_s.append(char)
                else:
                    word.replace(char, '')
            #print(new_s)
        answer_string = ('').join(new_s)
        #print(answer_string)
        answer = answer_string[:: -1]
        
        # print(answer)
        # print(answer_string
        # )

        if answer_string == answer:
            return True
        else:
            return False 
             
# EFFICIENT SOLUTION

def isPalindrom(s):
 
  left = 0
  right = len(s) -1
  
   # skip not alpanum char
  
  while left < right:
    if  not s[left].isalnum():
      left += 1
      continue
    
    if not s[right].isalnum():
      right -= 1
      continue
    
     # make lowercase
   
    if s[left].lower() != s[right].lower():
      return False
  
    left += 1
    right -= 1
    
  return True    
      
        

print(isPalindrom("A man, a plan, a canal: Panama"))

