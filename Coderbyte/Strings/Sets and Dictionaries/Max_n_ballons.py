# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

#You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Input: text = "nlaebolko"
# Output: 1

from collections import defaultdict



def maxNumberOfBalloons(text):
 
  balloon = 'ballon'
  # make dict of  string
  t_dict = {}
 
  for letter in text:
    if letter not in t_dict:
      t_dict[letter] = 1
    else:
      t_dict[letter] += 1
  
# check letter by letter can we make 'ballon'
 # if letter from ballon is missing in text
  if any (letter not in t_dict for letter in balloon):
    return 0
  else:
    # return lowest value in an iterable
    return min(t_dict['b'],t_dict['a'],t_dict['l']//2,t_dict['o']//2,t_dict['n'])
  
      


print(maxNumberOfBalloons( "loonbalxballpoon"))