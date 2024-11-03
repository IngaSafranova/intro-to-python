# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
def rotateString( s, goal):
  # make s a list
  string = list(s)
  # iterate and remove first letter
  for char in string:
    popped = string.pop(0)
     # put that letter at the back
    string.append(popped)
  # make a list into string again
    word = ('').join(string)
    
  # check is it the same as goal
    if word == goal:
      return True
  return False   
 

print(rotateString("abcde","cdeab"))