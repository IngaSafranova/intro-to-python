# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true

def containsDuplicate( nums):
  # set has only unique values
        nums_set = set()
        
        for number in nums:
            if number  in nums_set:
                return True
            else:
                nums_set.add(number)
        return False
      
print(containsDuplicate([1,2,3,4,1]))
        
