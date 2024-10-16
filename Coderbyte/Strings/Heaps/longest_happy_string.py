# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.

import heapq
class Solution(object):
    def longestDiverseString(self, a, b, c):
        # have max heap to store counts
        max_heap = []
        # have result list
        result = []

        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap,(-c, 'c')) 
        #print(max_heap)

        while max_heap:
            # take max count character
            count, char = heapq.heappop(max_heap)
            # make count positive integer again
            count = -count
            # check that we dont use the same char for the third time
            if (len(result) >=2 and result[-1] == char and result[-2] == char):
                # if no other char left in heap we break out of while loop
                if not max_heap:
                    break
            # if we have other characters to use we use them  
                next_count, next_char = heapq.heappop(max_heap)
                result.append(next_char)
                next_count = -next_count
                next_count -= 1
                #print(next_count)
                # if we still any char left we push back into heap
                if next_count > 0:
                    heapq.heappush(max_heap, ( -next_count , next_char))
            # if we still have other char in the heap and cannot use first char we push it back to the heap        
                heapq.heappush(max_heap, (-count, char))  
            else:
                # if we can use first char we use it
                count -= 1
                result.append(char)
                # if still have some left we push them back into heap for later use again
                if count > 0:
                    heapq.heappush(max_heap, (-count, char))
        return ''.join(result)                

