# You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

# Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.


# s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
from collections import deque

def areSentencesSimilar( sentence1, sentence2):
# put both sentences into queues
  s1 = deque(sentence1.split())
  s2 = deque(sentence2.split())
  print(s1)
# make sent1 be shorter
  if len(s1) > len(s2):
    s1,s2 = s2,s1
# while we have sent1 check first and last words
  while s1:
    # if they the same remove them and return true at the end
    if s1[0] == s2[0]:
      s1.popleft()
      s2.popleft()
    elif s1[-1] == s2[-1]:
      s1.pop()
      s2.pop()
    else:
      # if not return false
      return False
  return True  
        


  

print(areSentencesSimilar( "Hello Jane" ,"Hello my name is Jane"))