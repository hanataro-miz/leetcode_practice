# I used zyrastory's code as a reference.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        
        l = set()
        m = 0
        i = 0
        j = 0
    
        while(i < len(s)):
            if(s[i] not in l):
                l.add(s[i])
                i += 1
            else:
                m = max(m, len(l))
                l.remove(s[j])
                j += 1

        return max(m, len(l))
        
# Runtime: 90 ms, faster than 65.29% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14 MB, less than 49.30% of Python3 online submissions for Longest Substring Without Repeating Characters.
