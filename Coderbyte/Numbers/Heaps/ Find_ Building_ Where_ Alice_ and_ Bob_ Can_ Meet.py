# You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.

# If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].

# You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.

# Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

# Example 1:

# Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
# Output: [2,5,-1,5,2]
# Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2]. 
# In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5]. 
# In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
# In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
# In the fifth query, Alice and Bob are already in the same building.  
# For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
# For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.


##### BRUTE FORCE  not passing all test #####

from collections import defaultdict
from heapq import heappush
import heapq


def leftmostBuildingQueries(heights, queries):
  result = [-1] * len(queries)
  for index, height in enumerate(queries):
    # sort the queries so we have higher index on right
    left, right = sorted(height)
    print(left)
    
  # we need to find what is leftmost index for both queries to meet
  # if both querie indeses are the same, people are in the same building alredy
  # if queries right index height is higher than left index height, that`s where people can meet
    if left == right or heights[left] < heights[right]:
      result[index] = right
      continue
    
  # if not above both indeses heights needs to be lower than left most index height 
    for j in range(right + 1, len(heights)):
      if heights[j] > max(heights[left], heights[right]):
        result[index] = j
        break
      
  return result
  

#print(leftmostBuildingQueries([5,3,8,2,6,1,4,6],[[0,7],[3,5],[5,2],[3,0],[1,6]]))



def leftmostBuildingQueries(heights, queries):
  # keep in the dictionary each query max height and index - have right index as a key
  groups = defaultdict(list) # right -> query_height, query_index
  result = [-1]* len(queries)
  #sort queries heights and have left and right pointers for them
  for index, height in enumerate(queries):
    left, right = sorted(height)
    #print(right)
   # if both querie indeses are the same, people are in the same building alredy
  # if queries right index height is higher than left index height, that`s where people can meet 
    if left == right or heights[left] < heights[right]:
      result[index] = right
    else:
      # find max height for querie
      query_height = max(heights[left], heights[right])
      #print(query_height)
      # append to dictionary with index of the query
      groups[right].append((query_height,index))
  #print(groups)
      
  # have heap to keep data from queries groups   
  min_heap = []
  
  # iterate heights list
  for index, height in enumerate(heights):
    # iterate groups dictionary
    for query_height, query_index in groups[index]:
      # push data to heap
      heapq.heappush(min_heap,(query_height,query_index))
  
  # while heap is not empty we check the height from height ist with max_height from heap
  # if height is greater we found our answer for query
    while min_heap and height > min_heap[0][0]:
      # remove query from heap
      query_height, query_index = heapq.heappop(min_heap)
      # result at index of query_index is index of heights list
      result[query_index] = index
      
  return result
    

print(leftmostBuildingQueries([6,4,8,5,2,7],[[0,1],[0,3],[2,4],[3,4],[2,2]]))