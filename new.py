
def number(big_number_list):
 big_number_list = [1, 2, -1, 4, -5, 5, 2,-9]
 print(big_number_list)
# Print only positive numbers:
 for i in big_number_list:
  if i < 0:
   continue
 print(i)
 
 print(number(input()))