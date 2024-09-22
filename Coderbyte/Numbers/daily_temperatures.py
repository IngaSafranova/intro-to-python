# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

def dailyTemp(temp):
    n = len(temp)
    answer = [0]*n
    temp_stack =[] 
  # have temp and index
    for i,t in enumerate(temp):
   # check if temp in stack is less than one in temp list
        while temp_stack and temp_stack[-1][0] < t:
    # if yes pop it from the stack with the index
           temp_stack_t,temp_stack_i = temp_stack.pop()
      # substrack hihger temp index from index in stack and append answer list with the result.
           answer[temp_stack_i] = i - temp_stack_i
          
         # put temp into stack  
        temp_stack.append((t,i))
        
    return answer
        
  
    
    
      
    
  
  

print(dailyTemp([73,74,75,71,69,72,76,73]))