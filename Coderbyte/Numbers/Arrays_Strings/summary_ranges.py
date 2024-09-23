# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

def summaryRanges( nums):
        ans = []     
        i = 0 
       #loop and start with index 0 
        while i < len(nums): 
            start = nums[i] 
        # go through the nums and check if num+1 is equal to next num     
            while i < len(nums)-1 and nums[i] + 1 == nums[i + 1]: 
              # go to next if yes
                i += 1 
          # if not append to results list start and end of range  
            if start != nums[i]: 
                ans.append(str(start) + "->" + str(nums[i]))
            # if no range append number    
            else: 
                ans.append(str(nums[i]))
            
            i += 1

        return ans
        # Time: O(n)
        # Space: O(n) 
      
      
  


print(summaryRanges([0,1,2,4,5,7]))