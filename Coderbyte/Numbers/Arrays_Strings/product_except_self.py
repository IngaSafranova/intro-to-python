# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

      ##### 2 solutions #####
      
def productExceptSelf(nums):
  # go through array and multiply from left to right
  # the same from right to left
  # multiply those 2 arrays together index by index
  left_product = 1
  right_product = 1
  n = len(nums)
  # make arr with 0`s
  l_arr = [0] * n
  print(l_arr)
  r_arr = [0] * n
  
  for i in range(n):
    # get last index
    j = -i-1
    l_arr[i] = left_product
    r_arr[j] = right_product
    # print(l_arr)
    # print(r_arr)
    left_product *= nums[i]
    # print(left_product)
    right_product *= nums[j]
   
   # multiply both arr, zip() pairs arrays together 
    answer = [l * r for l, r in zip(l_arr, r_arr)]
    # print(answer)
  return answer
  
print(productExceptSelf([1,2,3,4]))

def productExceptSelf(nums):
  # same as above, multiply from left to right 
  # and right to left but keep answers in 1 answer array
  n = len(nums)
  answer = [0]*n
  left_product = 1
  right_product = 1
  
  # multiply from left
  for i in range(n):
    answer[i] = left_product
    left_product *= nums[i]
    
  # multiply from right
  for j in range(n-1,-1,-1):
    # we cannot reasign, we multiply left product with right product
    answer[j] *= right_product
    # find right product for each number
    right_product *= nums[j]
  return answer  
    
    
