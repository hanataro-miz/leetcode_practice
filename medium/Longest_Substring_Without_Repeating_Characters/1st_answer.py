class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length_list = []
        word_list = []
        length = 0
        
        for i in range(len(s)):
            for j in range(len(s) - i):
                if s[i + j] in word_list:
                    length_list.append(length)
                    word_list.clear()
                    length = 0
                    break
                else:
                    word_list.append(s[i + j])
                    length += 1
        length_list.append(length)
        return max(length_list) 

# Runtime: 4088 ms, faster than 5.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 13.34% of Python3 online submissions for Longest Substring Without Repeating Characters.
