# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3


def numJewelsInStones( jewels, stones):
  
  # make dict with all letters in it
  stone_dict = {}
  
  jewels_dict = {}
  sum = 0
  
  for letter in stones:
    if letter not in stone_dict:
      stone_dict[letter] =1
    else:
      stone_dict[letter] += 1  
      print(stone_dict)
      
  for letter in jewels:
    if letter not in jewels_dict:
      jewels_dict[letter] = 1
    else:
      jewels_dict[letter] += 1
  print(jewels_dict)
    # check does letter from stone string is in dict
  for letter in stone_dict and jewels_dict:  
    if letter in stone_dict and letter in jewels_dict:
      print(letter)
      sum += stone_dict[letter]
      print(sum)
  # return value if yes
  return sum
    
print(numJewelsInStones('aA','aAAbbb'))    
