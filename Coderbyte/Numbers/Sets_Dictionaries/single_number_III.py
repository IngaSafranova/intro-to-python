# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]

def singleNumber(nums):
  numbers = {}
  ans = []
  for num in nums:
    if num not in numbers:
      numbers[num] = 1
    else:
      numbers[num] += 1
  print(numbers) 
     
  for num,val in numbers.items():
    if val == 1:
      ans.append(num)
  return ans    
          
  

print(singleNumber([1,2,1,3,2,5]))