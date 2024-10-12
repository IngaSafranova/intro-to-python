# You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

# You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

# Return the minimum number of groups you need to make.

# Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.


# Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
# Output: 3
# Explanation: We can divide the intervals into the following groups:
# - Group 1: [1, 5], [6, 8].
# - Group 2: [2, 3], [5, 10].
# - Group 3: [1, 10].
# It can be proven that it is not possible to divide the intervals into fewer than 3 groups.

def minGroups(intervals):
  intervals.sort()
  #print(intervals)
  events = []
  summ = 0
  max_summ = 0
   # have events list to store (start, 1) and (end + 1, -1)
  for interval in intervals:
    events.append((interval[0], 1))
    events.append((interval[1]+1, -1))
  #print(events)  
  # sort the list
  events.sort()
  #print(events)
 # sum the end events and keep max
  for event in events:
    summ += event[1]
    #print(summ) 
    max_summ = max(max_summ, summ)
  return max_summ
  pass

print(minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))