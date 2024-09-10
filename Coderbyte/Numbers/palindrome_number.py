def isPalindrome(x):
        string = str(x)
        reversed_number = string[:: -1]
        print(reversed_number)
        if reversed_number == str(x) :
            return True
        else:
            return False  
          
          
print(isPalindrome(235))            