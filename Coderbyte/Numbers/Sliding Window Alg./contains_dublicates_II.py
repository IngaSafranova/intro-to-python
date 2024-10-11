# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Input: nums = [1,2,3,1], k = 3
# Output: true

def containsNearbyDuplicate(nums, k):
  i = 0
  for j in range(1,len(nums)):
    
    print(f'num[i] -{nums[i]}')
    print(f'num[j] - {nums[j]}')
    while nums[i] == nums[j]:
      print(f'num -i {i}')
      print(f'num-j {j}')
      w = abs(i-j)
      print(f'w - {w}')
      if w <= k:
        return True
      if w != k:
        i += 1
        print(f'l - {nums[i]}')
    #i += 1
    print(f't - {i}')
    print(f' jj - {j}')    
  return False    
  

print(containsNearbyDuplicate([1,0,1,1],1))