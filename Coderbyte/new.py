# def numbers(n):
#   for num in n:
#     if num < 0:
#       continue
#     print(num)
    
    
# print(numbers([1,2,-3,3,4]))
def ArrayChallenge(strArr):
    # define-ocg The variable 'varOcg' will store the number of differences
    varOcg = 0
    
    # Access the two strings from the array
    str1 = strArr[0]
    str2 = strArr[1]
    
    # Loop through each character in the strings
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            varOcg += 1  # Increment 'varOcg' if the characters are different
    
    return varOcg

# Example usage:
print(ArrayChallenge(["house", "hours"]))  # Output: 2
print(ArrayChallenge(["10011", "10100"]))  # Output: 3