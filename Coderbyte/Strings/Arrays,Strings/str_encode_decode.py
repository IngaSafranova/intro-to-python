# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]

def encode(strs):
  # have result string
  result = ''
   # iterate strings list
  for s in strs:
    
 # have a len(string) at the begining of strings to know how long the word needs to be when decoding back.
 # needs to be string type to concatenate
 # have some identifier to show the begining of word (as words may have numbers or symbols in them)
 # concatenate all in one string
    result += str(len(s)) + '#' + s
  print(result)
  return result 
 


print(encode(["neet","code","love","you"]))

def decode(s):
  # have result list
  result = []
  i = 0
   # iterate through string
  while i < len(s):
    # have i and j pointers at the same index at first - 0 whick is number
    j = i
     # check while j is not our identifier, move j to index of identifier
    while s[j] != '#':
      j += 1
     # extract lenght of string into number variable
    lenght_of_string = int(s[i:j])
    print(lenght_of_string)
      # # move i to position of first letter
    i = j+1
      # move j to position after the letter
    j = i + lenght_of_string
    result.append(s[i:j])
    i =j
  print(result) 
  return result 
  
 
  
 

  
  
  # append result list with extacted word
  # move i to position of j
  pass

print(decode('4#neet4#code4#love3#you'))