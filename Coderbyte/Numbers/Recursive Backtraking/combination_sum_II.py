# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
class Solution(object):
    def combinationSum2(self, candidates, target):
        nums = candidates
        # sort nums to avoid dublicates
        nums.sort()

        n = len(nums)
        result = []
        solution = []

        if not nums:
            return []
            
        def backtrack(start , curr_sum,target):
            if curr_sum == target:
                result.append(solution[:])
                return
            if curr_sum > target or start == n:
                 return 


            for i in  range(start,len(nums)):    
                if nums[i]> target:
                    break

                if curr_sum + nums[i] > target:
                    break
            # skip the dudlicates    
                if i > start and nums[i] == nums[i -1]:
                    continue
                
                solution.append(nums[i])
                backtrack(i+1 , curr_sum + nums[i],target)
                solution.pop()    


        backtrack(0,0, target)
        return result       