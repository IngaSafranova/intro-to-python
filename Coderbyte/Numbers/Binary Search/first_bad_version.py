# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Input: n = 5, bad = 4
# Output: 4

class Solution(object):
    def firstBadVersion(self, n):
     # left is first version, right is last version   
        left = 1
        right = n

        while left < right:
            middle = (left+right)//2
          # check is middle is first bad version  
            if isBadVersion(middle):
         # if yes we put right pointer on it as we dont want to loose it       
                right = middle
            else:
        # if not move left by one        
                left = middle +1
# when right and left will be same version we found the answer. We return either one
        return left            
            
   
print(firstBadVersion(5))