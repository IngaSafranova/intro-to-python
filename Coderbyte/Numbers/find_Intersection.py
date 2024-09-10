# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.




def FindIntersection(strArr):
  
  # make two sepatate arrays with each number as sepatate string
  string_1 = strArr[0].split(',')
  string_2 = strArr[1].split(',')
 # print(string_1)
  
  # do  list comprehension and look for same number in both lists
  intersection = ",".join([ number for number in string_1 if number in string_2])
  if len(intersection) == 0:
    intersection = "false"
  
  return intersection

# keep this function call here 
print(FindIntersection(['1,6,4', '5,6,1']))