#Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


def spiralOrder( matrix):
  # find how many columns are
  col = len(matrix)
   # find how many rows
  row = len(matrix[0])
  # keep track of visited rows and colums
  check = set()
  result = []
  
  row_begin = 0
  col_begin = 0
  
  while len(result) < col*row:
      
      while col_begin < row and (row_begin, col_begin) not in check:
          # check first row
          check.add((row_begin,col_begin))
          result.append(matrix[row_begin][col_begin])
          col_begin +=1
          print(f'check - {check}')
          print(f'result-{result}')
          #print(f'col {col_begin}')
          
      col_begin -= 1
      print(f'col {col_begin}')
      row_begin += 1
      print(f'row - {row_begin}')
  
  


print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
