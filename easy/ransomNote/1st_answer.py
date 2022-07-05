class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = []
        for i in range(len(magazine)):
            d.append(magazine[i])
        for i in range(len(ransomNote)):
            if ransomNote[i] in d:
                d.remove(ransomNote[i])
            else:
                return False
        return True
