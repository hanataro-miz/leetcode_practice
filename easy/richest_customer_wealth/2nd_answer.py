class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            if wealth > max_sum:
                max_sum = wealth
        return max_sum
