# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.




def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        even_list = []
        odd_list = []
        for n in nums:
            if n % 2 == 0:
                even_list.append(n)
                print(even_list)
            else:
                odd_list.append(n)
        result = even_list + odd_list
        print(result)
        return result