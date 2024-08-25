# Video alternative: https://vimeo.com/954334103/0aed500d39#t=0







example_numbers = [1, 2, 3, -2, -2, 2, None, -3, 4, 4, None, 3, 3, 2, 2, 1]

# Desired output:
# 1: xx
# 2: xxxxxx
# 3: xxxx
# 4: xx

def generate_frequency_graph(numbers):
  # * Gets rid of junk data
 integers = integers_only(numbers)
 # * Converts negative integers to positive numbers
 positives = convert_to_positives(integers)
 # * Creates a graph of how frequently each number shows up
 frequency_numbers = generate_frequency(positives)
 graph = format_graph(frequency_numbers)
 return graph

def integers_only(numbers):
 # * Gets rid of junk data
 int = []
 for number in numbers:
   if number != None:
     int.append(number)
 return int   

print('Function: integers_only')
print(integers_only([1,2,None,-4]))

def convert_to_positives(numbers):
  # * Converts negative integers to positive numbers
  positive_numbers = []
  for number in numbers:
    if number < 0:
      positive = number * -1
      positive_numbers.append(positive)
    else:
      positive_numbers.append(number)
  return positive_numbers    

print('Function: convert_to_positives')
print(convert_to_positives([1,2,4,-8,-4]))

def generate_frequency(numbers):
  # * Creates a graph of how frequently each number shows up
  frequency_dict = {}
  for number in numbers:
    if number not in frequency_dict:
      frequency_dict[number]=1
    else:
      frequency_dict[number] += 1
  return frequency_dict    


print('Function: generate_frequency')
print(generate_frequency([1,2,4,1,4,4,5]))

def format_graph(frequency_dict):
  
# Desired output:
# 1: xx
# 2: xxxxxx
# 3: xxxx
# 4: xx

 graph = ''
 for number in frequency_dict:
   graph += f"{number}: {'x' * frequency_dict[number]}\n"
 return graph  
   
print('Function: format_graph')
print(format_graph({1:2, 2:3, 3:1}))

print(generate_frequency_graph(example_numbers))