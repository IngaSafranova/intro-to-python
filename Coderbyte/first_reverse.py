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

def reverse(str):
  return str[::-1]

print(reverse('go to school!'))

# A slice bracket has three 'slots': Start, end, and step.

# [2:17:3] means: Start at 2, end before 17, go in steps of 3.

# [17:2:-3] means: Start at 17, end before 2, go *backward* steps of 3.

# If you leave slots empty, there's a default.

# [:] means: The whole thing. 

# [::1] means: Start at the beginning, end when it ends, walk in steps of 1 (which is the default, so you don't even need to write it).

# [::-1] means: Start at the end (the minus does that for you), end when nothing's left and walk backwards by 1.
