# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

def mySqrt(x):
  # use binary search to find which number is squared
  left = 0
  right = x
  while x <= right:
    middle = left + ((right - left)//2)
    if middle * middle == x:
      return middle
    elif middle * middle > x:
      right = middle -1
    else: left = middle + 1
  # if we cannot find our number as middle, we leave the loop as right starts to be less than left
  # we return right as we are asked to return nearest interger rounded down, so we return smaller number  
  return right    
    
  

print(mySqrt(4))