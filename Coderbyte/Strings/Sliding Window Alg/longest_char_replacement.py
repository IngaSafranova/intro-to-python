# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

def characterReplacement(s, k):
        count = {}
        l = 0 
        res = 0 
        
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            
            # check validity
  # if window length - max count is > k          
            while r - l + 1 - max(count.values()) > k:
                # shrink window 
                count[s[l]] -= 1
                l += 1
            
            res = max(res,r - l + 1)
        
        return res
                
print(characterReplacement("AABABBA",1))                
                
              
        
        
                
                