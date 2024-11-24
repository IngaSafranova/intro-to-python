# You are given an n x n integer matrix. You can do the following operation any number of times:

# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.

# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.


# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.

from math import inf


def maxMatrixSum(matrix):
  # count negative numbers
  # count absolute sum
  # keep track of minimum absolute number
  negative_count = 0
  absolute_sum = 0
  min_abs_number = inf
  rows = len(matrix)
  # traverse the matrix row by row
  for numbers in matrix:
    for number in numbers:
      absolute_sum += abs(number)
      min_abs_number = min(min_abs_number, abs(number))
      if number < 0:
        negative_count += 1
      #print(negative_count) 
      
 # if negative count is odd we cannot change all numbers to positive     
  if negative_count % 2 == 1:
    # so from absolute sum we take out min_abs_number *2
    # *2 because we added that number - 1) in hope of making it positive, so we take it out as its not positive,
    # 2) we take put again as we need to keep it out of sum as its negative
    absolute_sum -= 2 * min_abs_number
  return absolute_sum  
     
      
  
  

print(maxMatrixSum( [[1,2,3],[-1,-2,-3],[1,2,3]]))