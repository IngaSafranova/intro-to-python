# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above.

# Input: box = [["#","#","*",".","*","."],
#               ["#","#","#","*",".","."],
#               ["#","#","#",".","#","."]]
# Output: [[".","#","#"],
#          [".","#","#"],
#          ["#","#","*"],
#          ["#","*","."],
#          ["#",".","*"],
#          ["#",".","."]]
 

def rotateTheBox( box):
  # at the end row will be columns and columns will be rows
        rows = len(box)
        columns = len(box[0])
        result = []

        for row in range(rows):
          # set last cell in a row to indicate an empty spot
            i = columns -1
            #print(box[row])
          # iterate column backwards as after rotating rocks will fall down
            for col in reversed(range(columns)):
                if box[row][col] == '#':
            # if cell is a rock we swap with i - empty space, if i = rock, we just swap with itself      
                    box[row][col], box[row][i] = box[row][i], box[row][col]
                   # move i to next position 
                    i -= 1
            # if cell is a block     
                elif box[row][col] == '*':
                  # move empty space after the block
                    i = col -1
            #print(box) 
            
     # to populate result array       
        for col in range(columns):
            column = []  # this is a row after rotation
            
            for row in reversed(range(rows)):
                column.append(box[row][col])
            result.append(column)
        return result
                    


print(rotateTheBox([["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]))