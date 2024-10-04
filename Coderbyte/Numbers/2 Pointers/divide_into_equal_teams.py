# You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

# The chemistry of a team is equal to the product of the skills of the players on that team.

# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation: 
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

from curses.ascii import isdigit


def dividePlayers( skill):
  # if arr[] return -1
  if not skill:
    return -1
  n = len(skill)
  # if arr lenght -2 return the sum of it.
  if n == 2:
    return sum(skill)
  teams = []
  # sort the list
  skill.sort()
  # This is target number for a team
  team_target = skill[0] + skill[-1]
  # have 2 pointers to check if pl[0] + pl[-1] adds up to target
  left = 0
  right = n-1
  while left < right:
     # if yes append those to players to ans list
    if skill[left] + skill[right] == team_target:
      teams.append((skill[left],skill[right]))
      left += 1
      right -= 1
    else:
      return -1  
  
 # after iteration do calculations for answer
  ans = 0
  for i in teams:
    ans += (i[0]*i[1])
  return ans  
  
  

print(dividePlayers([2,4,1,3]))