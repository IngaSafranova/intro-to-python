# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

 # Input: ransomNote = "a", magazine = "b"
# Output: false

def canConstruct( ransomNote, magazine):
  
  magazine_dict = {}
  
      
  for letter in magazine:
    if letter not in magazine_dict:
      magazine_dict[letter] = 1
    else:
      magazine_dict[letter] += 1
      
  for letter in ransomNote:
    if letter not in magazine_dict:
      return False
    if letter in magazine_dict and magazine_dict[letter] > 1:
      magazine_dict[letter] -= 1
    else:
     if magazine_dict[letter] == 1:
      magazine_dict.pop(letter)
    
  return True
 
print(canConstruct('aah','abaaajjk'))