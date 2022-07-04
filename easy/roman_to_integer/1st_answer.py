def exchange(char: str) -> int:
    if char == "I":
        return 1
    if char == "V":
        return 5
    if char == "X":
        return 10
    if char == "L":
        return 50
    if char == "C":
        return 100
    if char == "D":
        return 500
    if char == "M":
        return 1000

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            interest = exchange(s[i])
            if i + 1 < len(s) and interest < exchange(s[i + 1]) :
                result -= interest
            else :
                result += interest
        return result
