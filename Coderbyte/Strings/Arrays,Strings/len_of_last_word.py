# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s):
     # make into list
       s1 = s.split()
     # find the lenght of last word  
       return len(s1[-1])
print(lengthOfLastWord('   I    go  to shool     '))     