# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

    ##### BRUTE FORCE #####
    
from curses import window


def decrypt(code,k):
  n = len(code)
  # keep result filled with 0 when k = 0
  result = [0]* n
  
  for i in range(n):
    if k > 0:
      # we need the sum of next k elements
      for j in range(i+1, i+k+1):
        
        # to make circular iteration --- i % n
        result[i] += code[j % n]
    else:
      for j in range(i-1, i-1-abs(k),-1):
        result[i] += code[j % n]
        #print(result[i])    
  return result    
  
print(decrypt([2,4,9,3], -2))  

##### SLIDING WINDOW #####

def bomb(code, k):
  n = len(code)
  result = [0]*n
  
  # have a sliding window lenght k
  left = 0
  current_sum = 0
  # use abs() if k < 0 n+k extends the array by k elements
  for right in range(n + abs(k)):
    # use modulus to make circular iteration
    current_sum += code[right % n]
    print(current_sum)
    window_lenght = right - left + 1
    print(window_lenght)
   
   # when window too big make smaller by shifting left 
    if window_lenght > abs(k):
      current_sum -= code[left % n]
      left = (left+1)% n
    
    if window_lenght == abs(k):
      if k > 0:
        result[(left -1) % n] = current_sum
      elif k < 0:
        result[(right + 1) % n] = current_sum
    
  return result
        
    
    
  pass

print(bomb([5,7,1,4], 3)) 