# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

def generateParenthesis(n):
  answer = []
  solution = []
  # have a count for open and close brackets
  def backtrack(open_b, closing_b):
    # if len(solution) = 2n, we used all the brackets
    if len(solution) == n*2:
      answer.append(('').join(solution))
      return
    # if we have open brackets less than n, we can use open bracket
    if open_b < n:
      solution.append('(')
      backtrack(open_b + 1,closing_b)
      solution.pop()
    
  # we can use closing bracket if its less than open brackets as we can close only open brackets
    if closing_b < open_b:
      solution.append(')')
      backtrack(open_b, closing_b + 1)
      solution.pop()  
  backtrack(0,0)
  return answer  
  
  
  

print(generateParenthesis(3))