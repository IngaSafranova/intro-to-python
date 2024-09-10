# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


def str( haystack, needle):
  result = haystack.find(needle)
  if result >= 0:
    return result
  else:
    return -1 
  
print(str('saddustnnnf','sab'))