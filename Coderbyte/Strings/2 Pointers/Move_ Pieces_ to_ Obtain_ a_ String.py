# You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

# The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
# The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
# Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

# Input: start = "_L__R__R_", target = "L______RR"
# Output: true
# Explanation: We can obtain the string target from start by doing the following moves:
# - Move the first piece one step to the left, start becomes equal to "L___R__R_".
# - Move the last piece one step to the right, start becomes equal to "L___R___R".
# - Move the second piece three steps to the right, start becomes equal to "L______RR".
# Since it is possible to get the string target from start, we return true.

def canChange(start, target):
  lenght = len(start)
  start_index = 0
  target_index = 0
  
  while start_index < lenght or target_index < lenght:
    while start_index < lenght and start[start_index] == '_':
      start_index += 1
    while target_index < lenght and target[target_index] == '_':
      target_index += 1
    if start_index == lenght or target_index == lenght:
      return (start_index == lenght and target_index == lenght)
    if (start[start_index] != target[target_index] or
        start[start_index] == 'L' and start_index < target_index or
        start[start_index] == 'R' and start_index > target_index):
      return False
    start_index += 1
    target_index += 1
    
  return True
  pass

print(canChange("_L__R__R_", "L______RR"))