# You are given an m x n binary matrix matrix.

# You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

# Return the maximum number of rows that have all values equal after some number of flips.

# Input: matrix = [[0,1],[1,1]]
# Output: 1
# Explanation: After flipping no values, 1 row has all values equal.

from collections import defaultdict
def maxEqualRowsAfterFlips( matrix):
  # we need to see how many rows we can make equal by inverting them
  # have a map to keep count of the same rows
  count = defaultdict(int)
  
  for row in matrix:
    
  # for the map key we can have a string of a row
    row_key = str(row)
    
    # if first number in a row is 1 we invert it
    if row[0]:
      row_key = str([0 if n == 1 else 1 for n in row ])
    count[row_key] += 1
    
  return max(count.values())
  
  
  pass

print(maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))
