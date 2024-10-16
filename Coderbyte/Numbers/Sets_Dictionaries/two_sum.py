# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

                        # 2 solutions #

def twoSum( nums,target):
        nums_dict = {}
        
        # make nums into dict, where list index is dict value and num is a key
        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        # to get second index substact number from target. One of the numbers will be the answer
        for i in range(len(nums)):
            y = target - nums[i]

            # check that second index is not the same as i.
            if y in nums_dict and nums_dict[y] != i:
                return [i, nums_dict[y]]
            
            
         ##### SECOND SOLUTION ####
         
            
         # have dict where we keep num as key and index as val
        nums_dict = {}  # num:index

        for index, num in enumerate(nums):
            #print(index,num)
            j = target - num
        # at first our map is empty and we check is number in the map    
            if j in nums_dict:
                return [nums_dict[j],index]
        # if number not good for the target we append to map, so when second number come up it will find first number in map. Map will not have every number from array if target numbers will be at the begining of array    
            nums_dict[num] = index 
        print(nums_dict)       


   
            
            

# Time Complexity: O(n)
# Space Complexity: O(n)
print(twoSum([3,2,3],6))