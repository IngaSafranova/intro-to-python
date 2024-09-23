# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

def mergeAlternately( word1, word2):
  
  # list is more eficient that string  
    merged = []
    A = len(word1)
    B = len(word2) 
    # use for looping through the words   
    a = 0
    b = 0
   # to switch between words
    word = 1 
    
    # use while loop to go through and concatenate letter by letter
    while a < A and b < B:
      if word == 1:
        merged.append(word1[a])
        a += 1
        word = 2
      else:
        merged.append(word2[b])
        b += 1
        word = 1     
    print(merged)        
        # if one word is longer put rest of letters at the end
    while a < A:
      merged.append(word1[a])
      a +=1
      
    while b < B:
      merged.append(word2[b])
      b += 1
    
    # join into string  
    return ('').join(merged)       
        
print(mergeAlternately('abcfg','pqr'))      