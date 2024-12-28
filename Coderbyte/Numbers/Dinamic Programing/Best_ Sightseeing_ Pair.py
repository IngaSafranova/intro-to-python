# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

# Return the maximum score of a pair of sightseeing spots.

# Example 1:

# Input: values = [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

##### BRUTE FORCE - TIME LIMIT #####

def maxScoreSightseeingPair(values):
        result = 0
        score_map = {}
        for i in range(len(values)):
        
            j = i+1
            while j < len(values):
                #print(values[i])
                #print(values[j])
                score = values[i] + values[j] + i - j
                score_map[i] = score
                j += 1
                #print(score_map)
                scores = score_map.values()
                #print(scores)
                max_scores = max(scores)
                #print(max_scores)
                result = max(result, max_scores)
                
        #print(result)
        return result

#print(maxScoreSightseeingPair([8,1,5,2,6]))

#### WORKING SOLUTION DYNAMIC PROGRAMING #####
def maxScoreSightseeingPair(values):
  result = 0
  # we start at index 0 as current max
  # tale -1 as that the distance to next number
  i = 0
  current_max = values[0] -1
  
  # we need to go check pairs backwards as we know previous numbers in the list
  for j in range(1, len(values)):
    # we check the sum of current value and previous value - distance between them
    
    result = max(result, current_max + values[j])
   # we need -1 for both values to increase the distance between numbers 
    current_max = max(current_max -1, values[j]-1)
    
  return result
  
  pass
print(maxScoreSightseeingPair([8,1,5,2,6]))