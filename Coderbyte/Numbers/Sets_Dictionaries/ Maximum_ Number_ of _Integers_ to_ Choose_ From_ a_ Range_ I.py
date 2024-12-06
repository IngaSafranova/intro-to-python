# You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

# The chosen integers have to be in the range [1, n].
# Each integer can be chosen at most once.
# The chosen integers should not be in the array banned.
# The sum of the chosen integers should not exceed maxSum.
# Return the maximum number of integers you can choose following the mentioned rules.
from collections import defaultdict

def maxCount( banned, n, maxSum):
  # make banned a map for better access
  banned_numbers = defaultdict(int)
  numbers = []
  count = 0
  for number in banned:
    banned_numbers[number] = 1
  for number in range(1, n + 1):
    numbers.append(number)
 # print(numbers)  
  for number in numbers:
    if number not in banned_numbers:
      maxSum -= number
     # print(maxSum)
      if maxSum >= 0:
        count += 1
      else:
        break
  return count
  
  
  pass

print(maxCount([1,6,5],5,6))