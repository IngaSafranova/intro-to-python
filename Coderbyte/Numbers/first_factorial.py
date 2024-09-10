# FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.

def FirstFactorial(num):

 if num == 1:
  return num
 return (num * FirstFactorial(num-1))
  

# keep this function call here 
print(FirstFactorial(8))

def FirstFactorial_1(num):
  result = 1
  for number in range(1, num + 1):
     result = result * number 
  return result  
    
    
print(FirstFactorial_1(8))   