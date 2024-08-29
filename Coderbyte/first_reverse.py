# First Reverse
 #Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH
 
def FirstReverse(strParam):
  # convert string to list
 new_list =[strParam]
 new_string_list = []
 result_list = ''
 # go throught list
 for words in new_list:
   # go through single words in the list
   for char in words:
     # insert each letter at the begining 
    new_string_list.insert(0,char)
 print(new_string_list)
 # convert back to string
 for char in new_string_list:
     result_list += f'{char}'
 print(result_list)
 return result_list  
 
 
 
   
   
 
    

# keep this function call here 
print(FirstReverse("I Love Code"))