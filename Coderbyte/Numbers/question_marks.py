# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
import re

def QuestionsMarks(strParam):
  
  # go through string untill first number found
  # put to separate list
  # check next char in the string, if ? put to list also if number put to list.
  # go througn new list and if int put to new list if ? count them
  # if next in line after ?= 3 is digit put to new list and add the up.
  # if sum = 10 return true
  
  
  # put to separate list
  new_list = []
 
  # go through string untill first number found
  for char in strParam:
     number = re.findall('[0-9]', char)
      # check next char in the string, if ? put to list also if number put to list.
     if number:
      new_list.append(int(char)) 
     if char == '?'and len(new_list) >=1:
       new_list.append(char) 
  print(new_list)
   # go througn new list and if int put to new list if ? count them
   # if next in line after ?= 3 is digit put to new list and add the up.
  # if sum = 10 return true
  numbers_list = []
  count = 0
  sum =0
  for char in new_list:
    if type(char) == int:
      numbers_list.append(char)
    if char == '?' :
      count += 1
    if count == 3 and len(numbers_list) == 2:
      sum = numbers_list[0]+ numbers_list[1]
      if sum == 10:
        return True
      elif sum != 10 and count == 3:
        count = 0
        numbers_list.remove(numbers_list[0])
      
  else:
      return False
  
  
  #return strParam

# keep this function call here 
print(QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5"))