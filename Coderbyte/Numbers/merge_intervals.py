# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

def merge(intervals):
  # sort intervals
  intervals.sort(key = lambda interval:interval[0])
  merged = []
  
  for int in intervals:
    # check if last merged int is less that current int
    if not merged or merged[-1][1] < int[0]:
      # if yes append current interval
      merged.append(int)
      print(merged)
    else:
     # if not keep last int first digit and replace second with which ever is greater: last digit or current int 
      merged[-1] = [merged[-1][0], max(merged[-1][1],int[1])]
      print(merged)  
  return merged    
  
  

print(merge([[1,3],[2,6],[8,10],[15,18]]))