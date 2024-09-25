# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

def isSquare(num):
  left = 1
  right = num
  
  while left <= right:
    m = left+((right-left)//2)
    m_squared = m*m
    
    if m_squared == num:
      return True
    elif m_squared < num:
      left = m +1
    else:
      right = m-1
  return False      
  

print(isSquare(16))