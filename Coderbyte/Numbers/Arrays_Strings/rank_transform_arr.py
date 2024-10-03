# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

class Solution(object):
    def arrayRankTransform(self, arr):
        if not arr:
            return []
        if len(arr) == 1:
            return [1]    
        # have array in list as val,index pairs
        new = [(val,ind) for ind,val in enumerate(arr)]
        # sort it
        new.sort()
        #print(new)
        rank =1

        # prev value
        previous = new[0][0]
       # print(previous)
        for i in range(len(arr)):
            if previous < new[i][0]:
                rank += 1

        # insert rank into array at index kept in new arr        
            arr[new[i][1]] = rank
            previous = new[i][0]

        return arr       
           

