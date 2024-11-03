# Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

# Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.

import re

def MinWindowSubstring(strArr):

# make 2 separate strings
 str_1 = strArr[0].split(',')
 str_text = str_1[0]
 print(str_text)
 str_2 = strArr[1].split(' ')
 patern = str_2[0]
 print(patern)
 
 index = []
 for char in range(len(patern)):
   if patern[char] in str_text:
     index.append(str_text.find(patern[char])) 
     
 print(index) 
 index.sort()  
 # save first index in l
 l = len(index)
 low = int(index[0])
 
# save  last index in h
 high = int(index[l-1])
 h = high +1
 for i in range(low,h):
    print(str_text[i],end=" ")
    
    
print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))