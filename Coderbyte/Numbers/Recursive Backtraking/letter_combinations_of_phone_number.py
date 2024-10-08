# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def letterCombinations(digits):
  # have a dict with numbers and letter values
  char_dict = {
    '2':'abc',
    '3':'def',
    '4':'ghi',
    '5':'jkl',
    '6':'mno',
    '7':'pqrs',
    '8':'tuv',
    '9':'wxyz'
    
  }
  if digits == '':
    return []
  n = len(digits)
  result = []
  solution = []
  
  # start at index 0
  def backtrack(i = 0):
    # if we at the end of traversing given numbers
    if i == n:
      result.append(''.join(solution))
      return
      
  # loop trought char_dict and for digit extract values
    for letter in char_dict[digits[i]]:
        solution.append(letter)
        # go to next digit
        backtrack(i + 1)
        solution.pop()
      
          
    pass
  backtrack(0)
  return result
  
  pass

print(letterCombinations('23'))