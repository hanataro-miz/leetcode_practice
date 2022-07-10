class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_list = []
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            sum_list.append(wealth)
        return max(sum_list)
