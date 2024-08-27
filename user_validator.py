# Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

# If the username is valid then your program should return the string true, otherwise return the string false.


def CodelandUsernameValidation(strParam):
  
    test1 = False
    test2 = False
    test3 = False
    test4 = True
    

    # 1. The username is between 4 and 25 characters.
    if len(strParam) >=4 and len(strParam) <=25:
       test1 = True
  
   
    # 2. It must start with a letter.
    if strParam[0].isalpha(): 
       test2 = True
    # 3. It cannot end with an underscore character.
    if '_' != strParam[-1]:
     test3 = True
    # 4. It can only contain letters, numbers, and the underscore character.
    # 
    for char in strParam:
      if not char.isalnum() and char != '_': 
            test4 = False 

     
    if test1 and test2 and test3 and test4:
     return  True
    else:
     return  False  

# keep this function call here 
print(CodelandUsernameValidation('ass@677kj_k'))