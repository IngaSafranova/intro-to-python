# Given a string word, compress it using the following algorithm:

# Begin with an empty string comp. While word is not empty, use the following operation:
# Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
# Append the length of the prefix followed by c to comp.
# Return the string comp.

def compressedString(word):
  comp = []
  n = len(word)
  i = 0
  
  while i < n:
    #print(word[i])
    char = word[i] 
    count = 0
    while i < n and word[i] == char and count < 9:
      count += 1
      i += 1
    comp.append(str(count))
    comp.append(char)
    print(comp) 
  return ('').join(comp) 
  

print(compressedString("aaaaaaaaaaaaaabb"))