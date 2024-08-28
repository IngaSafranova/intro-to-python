# Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

def BracketMatcher(strParam):

# count brackets
 brakets1 = strParam.count("(")
 brakets2 = strParam.count(")")
 
 # if brackets ok return 1
 # if not return 0
# if no brakets return 1
 if brakets1 == brakets2:
   return 1
 else:
   return 0


# keep this function call here 
print(BracketMatcher("(coder)(byte))"))