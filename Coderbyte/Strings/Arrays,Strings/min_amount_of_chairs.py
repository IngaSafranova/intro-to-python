# You are given a string s. Simulate events at each second i:

# If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
# If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
# Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.

# Input: s = "ELELEEL"

# Output: 2

# Explanation:

# Let's consider that there are 2 chairs in the waiting room. The table below shows the state of the waiting room at each second.

def minimumChairs(s):
  # keep track of people comming and leaving
  count = 0
  max_count = 0
  
  for char in s:
    if char == 'E':
      count += 1
    else:
      count -= 1
   # max count will show max number of people at any given time
    max_count = max(max_count, count)
    print(max_count)
  return max_count
  
print(minimumChairs("ELELEEL"))  