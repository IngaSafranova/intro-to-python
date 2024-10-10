# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

def maxWidthRamp(nums):
    
        n = len(nums)
        right_max = [0] * n

        # Fill right_max array with the maximum values from the right
        right_max[n - 1] = nums[n - 1]
        print(right_max)
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])
        print(right_max)

        left = 0
        right = 0
        max_width = 0

        # Traverse the array using left and right pointers
        while right < n:
            # Move left pointer forward if current left exceeds right_max
            while left < right and nums[left] > right_max[right]:
                left += 1
            max_width = max(max_width, right - left)
            right += 1

        return max_width  
 
  

print(maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))