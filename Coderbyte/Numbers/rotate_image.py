# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# [1 2 3]     [7 4 1]
# [4 5 6] =>  [8 5 2]
# [7 8 9]     [9 6 3]

def rotate( matrix):
  n = len(matrix)
  
  # do transpose - make a row into a column
  for i in range(n):
    # limit the range so the code will not do transpose twice
    for j in range(i ,n):
      
      matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    print(matrix)
      # [1,4,7][2,5,8][3,6,9]
      
      # reverse elements
    for i in range(n):
      for j in range(n//2):
       matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]
  return matrix
  
print(rotate([[1,2,3],[4,5,6],[7,8,9]]))