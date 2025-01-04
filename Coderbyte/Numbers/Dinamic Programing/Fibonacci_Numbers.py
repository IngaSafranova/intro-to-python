#### NORMAL RECURCION ####

def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib(n-2) + fib(n-1)
  
print(fib(5))

#####   TOP-DOWN MEMOIZATION ####

def fib1(n):
  # to optimize we can save function call in a dictionary
  # now we dont need to calculate same function calls many times
  # we take results from the dictionary if they exist
  
  dp = {
    0:0, 1:1
  } # n -> fuction call result
  
  # have a helper function to fill dict
  def f(x):
    # if result in dp return that
    if x in dp:
      return dp[x]
    else:
      # calculate function call and store in dp
      dp[x] = f(x-1) + f(x-2)
      
      return dp[x]
    # call helper function
  return f(n)
      
print(fib1(6))

##### BOTTOM-UP TABULATION #####

def fib2(n):
  # in this approach we create a list (table) and fill in the results
  # we start from bottom - 0 and go up till last number
  if n == 0:
     return 0
  if n == 1:
    return  1
  
  # create the list of size n + 1 for efficiency straight away
  # n+1 as array starts at index 0
  table = [0] * (n + 1)
  table[0] = 0
  table[1] = 1
  
  # we start at number 2 n+1 to get n as range is not inclusive of last number
  for i in range(2, n+1):
    # add 2 previous results
    table[i] = table[i -2] + table[i -1]
    
  return table[n]

print(fib2(8))

#### CONSTANT SPACE SOLUTION ###

def fib3(n):
  
  if n == 0:
    return 0
  if n == 1:
    return 1
  
  # to make constance space we dont have a table
  previous = 0
  current = 1
  
  for i in range(2, n+1):
    # at the same time we set previous to current
    # and current to previous + current
    previous, current = current, current + previous
    
  return current

print(fib3(9))