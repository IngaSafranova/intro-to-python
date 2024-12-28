# Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

# Example 1:

# Input: nums = [1,2,1,2,6,7,5,1], k = 2
# Output: [0,3,5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

def maxSumOfThreeSubarrays( nums, k):
        # using sliding window calculate all posible k lenght sums of the list
        k_sum = [sum(nums[:k])]

        for i in range(k,len(nums)):
            k_sum.append(k_sum[-1] + nums[i] - nums[i-k])
       # print(k_sum)
       # keep calculations from helper function in dinamic programing dict
        dp = {}
       # helper function to calculate max sum of subarrays from k_sum list
       # we use index of k_sum and count as parameters
        def get_max_sum(i,count):
            if count == 3 or i > len(nums) - k:
                return 0
            if (i, count) in dp:
                return dp[(i, count)]
        # Include into count at this index
            include = k_sum[i] + get_max_sum(i + k, count + 1)
        # Skip
            skip = get_max_sum(i + 1, count)
        # we save in dp the max sum from include and skip calculations
            dp[(i,count)] = max(include,skip)
           # print(dp)

            return dp[(i,count)]
    # helper function to get indeces of chosen sums
        def get_indeces():
            i = 0
            indeces = []

            while i <= len(nums) - k and len(indeces) < 3:
                include = k_sum[i] + get_max_sum(i + k, len(indeces) + 1)
                skip = get_max_sum(i + 1, len(indeces))

                if include >= skip:
                    indeces.append(i)
                    i += k
                else:
                    i += 1
            return indeces
        return get_indeces()
print(maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))