# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums):
        numbers = {}

        for num in nums:
            if num not in numbers:
                numbers[num] = 1
            else:
                numbers[num] += 1
        #print(numbers)

        for num, val in numbers.items():
            if val == 1:
                return num   