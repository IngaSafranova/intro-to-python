# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


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

# Time Complexity: O(n)
# Space Complexity: O(n)
print(twoSum([3,2,3],6))