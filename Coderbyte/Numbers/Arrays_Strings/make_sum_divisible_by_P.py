# Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

# A subarray is defined as a contiguous block of elements in the array.

# Input: nums = [3,1,4,2], p = 6
# Output: 1
# Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

class Solution(object):
    def minSubarray(self, nums, p):
    
    # Calculate the total sum of the array
        total_sum = sum(nums)
    
    # Target remainder when the total sum is divided by p
        remainder = total_sum % p
    
    # If the total sum is already divisible by p, no subarray needs to be removed
        if remainder == 0:
            return 0
    
    # Dictionary to store the latest index of prefix sums mod p
        prefix_sums = {0: -1}  # Initialize with 0 at index -1 to handle edge cases
        current_sum = 0
        min_length = len(nums)
    
    # Iterate through the array
        for i, num in enumerate(nums):
            current_sum += num
            current_mod = current_sum % p
        
        # The remainder we need to find in the prefix sums dictionary
            target_mod = (current_mod - remainder) % p
            #print(target_mod)
        
        # Check if the target_mod exists in the prefix sums
            if target_mod in prefix_sums:
            # Calculate the length of the subarray that needs to be removed
                min_length = min(min_length, i - prefix_sums[target_mod])
        
        # Update the prefix sums dictionary with the current mod value and its index
            prefix_sums[current_mod] = i
            #print(prefix_sums)
    
    # If no valid subarray was found, return -1
        return min_length if min_length < len(nums) else -1
