# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

import heapq

def kClosest( points, k):
  heap = []
    # formula for distace from the center
            # d = x**2 + y**2
  for x,y in points:
    d = x**2 + y**2          
    # make max heap of given points and distaces
    # until len(heap) < k just push
    if len(heap) < k:
      heapq.heappush(heap,(-d,x,y))
    else:
      # after pushpop so heaps lenght is k long 
      heapq.heappushpop(heap,(-d,x,y))
  #print(heap) 
  return [(x,y) for d,x,y in heap ]  
    
   
    # return points from the heap        
        
print(kClosest([[1,3],[-2,2]],1))      