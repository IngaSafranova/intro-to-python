# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].


def plusOne(digits):
        n = len(digits)
        if n == 1:
            if digits[0] < 9:
                digits[0] = digits[0] + 1
            else:
                digits.append(0)
                digits[n-1] = 1
            return digits 
        
        # iterate from back to start
        for i in range(n-1, -1,-1):
            #print(digits[i])
        # if digit is 9 make 0
            if digits[i] == 9:
                 digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
      # if all 9 in array prepend 1 at the start          
        return [1] + digits             
                
print(plusOne([9,9,9]))   
        