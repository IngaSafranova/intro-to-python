# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

def searchMatrix( matrix, target):
  left = 0
  n = len(matrix)
  right = n-1
  while left <= right:
    middle = (left + right)//2
   # search middle row 
    for num in matrix[middle]:
  # if num in this row return true
      if num == target:
        return True
  # if not check is target is less than first num in the row
  # if yes look at left rows
  # else look at right rows
  
      elif matrix[middle][0] > target:
        right = middle -1
      else:
        left = middle +1
  # if no target      
  return False      
  
  
 

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],31))