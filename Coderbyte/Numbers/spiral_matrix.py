#Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


def spiralOrder( matrix):
  # find how many columns are
  col = len(matrix[0])
   # find how many rows
  row = len(matrix)
  # keep track of visited rows and colums
  check = set()
  result = []
  
  row_index = 0
  col_index = 0
  
  while len(result) < col*row:
      
      while col_index < col and (row_index, col_index) not in check:
          # check first row
          check.add((row_index,col_index))
          # add first row
          result.append(matrix[row_index][col_index])
          col_index +=1
          print(f'c1 - {col_index}')
          print(f'check1 - {check}')
          print(f'result1-{result}')
      
      # col index needs to be backed to [2] as it is out of range after last iteration    
      col_index -= 1
      print(f'col1- {col_index}')
      # go to second row
      row_index += 1
      print(f'row1 - {row_index}')
      # go down at last col_index
      while row_index < row and (row_index, col_index) not in check:
          check.add((row_index,col_index))
          print(f'check2 - {check}')
          # append all last col_indexes
          result.append(matrix[row_index][col_index])
          print(f'result2-{result}')
          row_index += 1
          print(f'r2 - {row_index}')
          
      # bring back row_index from out of range to index[2]    
      row_index -=1 
      print(f'row2 - {row_index}')
      # move column_index forwards [1]
      col_index -= 1
      print(f'col2 - {col_index}')
      
      # while on last row check colums from greater to lower indexes
      while col_index >= 0 and (row_index, col_index) not in check:
          check.add((row_index, col_index))
          print(f'check 3 -{check}')
          result.append(matrix[row_index][col_index])
          print(f'tesulr3 - {result}')
          col_index -= 1
          print(f'c3 - {col_index}')
      
      # back to range    
      col_index += 1 
      print(f'col4 = {col_index}')
      # go row up
      row_index -= 1
      print(f'row4 - {row_index}')
  while row_index >= 0 and (row_index, col_index) not in check:
      check.add((row_index, col_index))
      result.append(matrix[row_index][col_index])
      row_index -=1

# back both indexes to range       
  row_index += 1
  col_index += 1
      
  print(f'final result - {result}')
  return result     
  
  


print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
