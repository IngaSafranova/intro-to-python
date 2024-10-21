# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 
from ast import Set
from collections import defaultdict


def isValidSudoku(board):
  # have sets to keep unique numbers
  rows = defaultdict(set)
  columns = defaultdict(set)
  squares = defaultdict(set) # key = (row//3, col//3)
  # check each column has unique numbers
  for col in range(9):
    
    # check rows and squares
    for row in range(9):
      if board[col][row] == '.':
        continue
      if (board[col][row] in rows[row] or board[col][row] in columns[col] or board[col][row] in squares[col//3,row//3]):
        return False
      
      rows[row].add(board[col][row])
      #print(rows)
      columns[col].add(board[col][row])
      squares[col//3,row//3].add(board[col][row])
  print(rows) 
  print(f'col - {columns}')   
  return True    
  

  pass 

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))