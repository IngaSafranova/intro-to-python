# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

# It is ().
# It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# It can be written as (A), where A is a valid parentheses string.
# You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

# If locked[i] is '1', you cannot change s[i].
# But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string. Otherwise, return false.

def canBeValid( s, locked):
        n = len(s)
        # if lenghts is odd
        if n % 2 == 1:
            return False
        open_brackets = []
        unlocked_brackets = []
    # check all brackets from left to right
        for i in range(n):
            # if unlocked put to this stack
            if locked[i] == '0':
                unlocked_brackets.append(i)
            # if '(' - put to open parentasis stack
            elif s[i] == '(':
                open_brackets.append(i)
                #print(open_brackets)
            else:
            # if we have closing bracket - ')'
                # check for open bracket
                if open_brackets:
                    open_brackets.pop()
                # check for unlocked bracket
                elif unlocked_brackets:
                    unlocked_brackets.pop()
                else:
                #if nothing available
                    return False
        #print(unlocked_brackets)
        
    # check the rest of open brackets and unlocked brakets
    # while they both not empty and index of open bracket is less than index of unlocked bracket:
        while open_brackets and unlocked_brackets and open_brackets[-1] < unlocked_brackets[-1]:
            open_brackets.pop()
            unlocked_brackets.pop()

        # if some open brackets left not used    
        if open_brackets:
            return False
# we checked at the begining for lenght to be even, so even if some unlocked brackets left, it will be even number so its true we can make valid parenthasis
        return True
print(canBeValid("))()))","010100"))